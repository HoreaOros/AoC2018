#region Input parsing
using System.Runtime.Serialization;

string text = File.ReadAllText("input.txt");
string[] lines = text.Split(Environment.NewLine);
int LIN = lines.Length;
int COL = lines[0].Length;
char[,] map = new char[LIN, COL];
int[] dr = { -1, 0, 1, 0 };
int[] dc = { 0, 1, 0, -1 };
List<Unit> units = new List<Unit>();
for (int i = 0; i < LIN; i++)
    for (int j = 0; j < COL; j++)
    {
        map[i, j] = lines[i][j];
        if (map[i, j] == 'G' || map[i, j] == 'E')
            units.Add(new Unit() { Type = map[i, j], R = i, C = j, HitPoints = 200, AttackPower = 3 });
    }


void PrintMap(char[,] map)
{
    for (int i = 0; i < LIN; ++i)
    {
        for (int j = 0; j < COL; ++j)
            Console.Write(map[i, j]);
        Console.WriteLine();
    }
    Console.WriteLine();
}
#endregion

#region Part1
int  Part1(List<Unit> units, char[,] map)
{
    int rounds = 0;
    while (true)
    {
        units.Sort(new ReadingOrder());

        bool fullRound = true;
        foreach (Unit unit in units)
        {
            if (unit.IsAlive)
            {
                // try attack neigh
                List<Unit> enemies = unit.GetAdjacentEnemies(map, LIN, COL, units);
                if (enemies.Count > 0)
                {
                    // attack
                    enemies.Sort(new ReadingOrder());
                    int minHP = enemies.Min(x => x.HitPoints);
                    Unit u = enemies.First(x => x.HitPoints == minHP);
                    u.Attack(map, unit.AttackPower);
                }
                else
                {
                    List<Unit> possibleTargets = unit.FindPossibleTargets(map, LIN, COL, units);
                    if (possibleTargets.Count == 0) continue;

                    HashSet<(int r, int c)> inRange = new();
                    foreach (Unit target in possibleTargets)
                    {
                        target.AddInRangeCells(inRange, map, LIN, COL);
                    }
                    HashSet<(int r, int c)> reachable = new HashSet<(int r, int c)>(inRange.Where(x => unit.IsPathTo(x, map, LIN, COL)));
                    HashSet<(int r, int c, int dist)> reachableWithDistance = unit.GetDistances(reachable, map, LIN, COL);
                    int minDistance = reachableWithDistance.Min(x => x.dist);

                    List<(int r, int c, int dist)> reachableWithMINDistance = new(reachableWithDistance.Where(x => x.dist == minDistance));
                    reachableWithMINDistance.Sort(new ReadingDistanceComparer<(int r, int c, int dist)>());
                    (int r, int c, int dist) chosenTarget = reachableWithMINDistance.First();


                    List<(int r, int c)> steps = new();
                    for (int k = 0; k < 4; k++)
                    {
                        int nr = unit.R + dr[k];
                        int nc = unit.C + dc[k];
                        if (nr >= 0 && nr < LIN && nc >= 0 && nc < COL)
                            if (map[nr, nc] == '.' && IsPath((chosenTarget.r, chosenTarget.c), (nr, nc), map) == minDistance - 1)
                                steps.Add((nr, nc));
                    }


                    steps.Sort(new ReadingOrder<(int r, int c)>());
                    (int r, int c) step = steps.First();
                    map[step.r, step.c] = map[unit.R, unit.C];
                    map[unit.R, unit.C] = '.';
                    unit.R = step.r;
                    unit.C = step.c;


                    // attack
                    List<Unit> enemies2 = unit.GetAdjacentEnemies(map, LIN, COL, units);
                    if (enemies2.Count > 0)
                    {
                        // attack
                        enemies2.Sort(new ReadingOrder());
                        int minHP = enemies2.Min(x => x.HitPoints);
                        Unit u = enemies2.First(x => x.HitPoints == minHP);
                        u.Attack(map, unit.AttackPower);
                    }


                }
            }
        }
     
        if (fullRound)
        {
            rounds++;

        }

        // if no more Elfs or Goblins break;
        int elfs = units.Count(x => x.Type == 'E' && x.IsAlive);
        int goblins = units.Count(x => x.Type == 'G' && x.IsAlive);
        if (elfs == 0 || goblins == 0)
            break;
    }
    return rounds;
}

int IsPath((int r, int c) start, (int r, int c) end, char[,] map)
{
    if (start == end)
        return 0;
    HashSet<(int r, int c)> seen = new();
    Queue<(int r, int c, int dist)> q = new();
    seen.Add((start.r, start.c));
    q.Enqueue((start.r, start.c, 0));

    while (q.Count > 0)
    {
        (int r, int c, int dist) = q.Dequeue();


        for (int k = 0; k < 4; k++)
        {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr >= 0 && nr < LIN && nc >= 0 && nc < COL)
            {
                if ((nr, nc) == end)
                    return dist + 1;
                if (!seen.Contains((nr, nc)) && map[nr, nc] == '.')
                {
                    seen.Add((nr, nc));
                    q.Enqueue((nr, nc, dist + 1));
                }
            }
        }
    }
    return -1;
}




#endregion

#region Part2

int allElfs = units.Count(x => x.Type == 'E' && x.IsAlive);
int allGoblins = units.Count(x => x.Type == 'G' && x.IsAlive);
Console.WriteLine($"Elfs: {allElfs} - Goblins: {allGoblins}");
int elfAttackPower = 4;
List<Unit> units1 = null;
int rounds = 0;
while(true)
{
    units1 = new List<Unit>();
    foreach(Unit unit in units)
    {
        int attackPower = unit.Type == 'E' ? elfAttackPower : 3;
        units1.Add(new Unit() {Type = unit.Type, R = unit.R, C = unit.C, HitPoints = unit.HitPoints, AttackPower = attackPower});
    }
    char[,] map1 = new char[LIN, COL];
    for (int i = 0; i < LIN; i++)
        for (int j = 0; j < COL; j++)
            map1[i, j] = map[i, j];
    rounds = Part1(units1, map1);
    int remaingElfs = units1.Count(x => x.Type == 'E' && x.IsAlive);
    int remainingGoblins = units1.Count(x => x.Type == 'G' && x.IsAlive);

    Console.WriteLine($"Elf attack power: {elfAttackPower} - Remaining Elfs: {remaingElfs}, Remaining Goblins: {remainingGoblins}");
    if (remaingElfs == allElfs && remainingGoblins == 0)
        break;
    elfAttackPower++;
}
Console.WriteLine(elfAttackPower);

int totalHP = units1.Where(x => x.IsAlive).Sum(x => x.HitPoints);
Console.WriteLine($"Rounds: {rounds} / Total HP: {totalHP}"); // number of full rounds is <rounds> - 1 ????
Console.WriteLine($"{(rounds - 1) * totalHP}");

#endregion

class Unit
{
    private static int[] dr = { -1, 0, 1, 0 };
    private static int[] dc = { 0, 1, 0, -1 };
    public char Type { get; set; } // G or E
    public int R { get; set; }
    public int C { get; set; }
    public int HitPoints { get; set; }
    public int AttackPower { get; set; }
    public bool IsAlive => HitPoints > 0;
    public override string ToString()
    {
        return $"{Type} ({R}, {C}, HP = {HitPoints})";
    }

    internal void AddInRangeCells(HashSet<(int r, int c)> inRange, char[,] map, int LIN, int COL)
    {
        for (int k = 0; k < 4; k++)
        {
            int nr = R + dr[k];
            int nc = C + dc[k];
            if (nr >= 0 && nr < LIN && nc >= 0 && nc < COL && map[nr, nc] == '.')
                inRange.Add((nr, nc));
        }
    }

    internal void Attack(char[,] map, int damage)
    {
        HitPoints -= damage;
        if (HitPoints <= 0)
            map[R, C] = '.';
    }

    internal List<Unit> FindPossibleTargets(char[,] map, int LIN, int COL, List<Unit> units)
    {
        HashSet<Unit> result = new();

        char enemy = this.Type == 'E' ? 'G' : 'E';
        Queue<(int r, int c)> q = new();
        HashSet<(int r, int c)> seen = new();
        q.Enqueue((R, C));
        seen.Add((R, C));

        while (q.Count > 0)
        {
            (int r, int c) = q.Dequeue();


            for (int k = 0; k < 4; k++)
            {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < LIN && nc >= 0 && nc < COL)
                {
                    if (!seen.Contains((nr, nc)) && map[nr, nc] == '.')
                    {
                        q.Enqueue((nr, nc));
                        seen.Add((nr, nc));
                    }
                    if (!seen.Contains((nr, nc)) && map[nr, nc] == enemy)
                    {
                        seen.Add((nr, nc));
                        Unit? unit = units.Find(x => x.R == nr && x.C == nc && x.IsAlive && x.Type == enemy);
                        if (unit != null)
                            result.Add(unit);
                    }
                }
            }
        }


        return new List<Unit>(result);
    }

    internal List<Unit> GetAdjacentEnemies(char[,] map, int LIN, int COL, List<Unit> units)
    {
        List<Unit> lst = new List<Unit>();
        char enemy = this.Type == 'E' ? 'G' : 'E';
        for (int k = 0; k < 4; k++)
        {
            int nr = this.R + dr[k];
            int nc = this.C + dc[k];

            if (nr >= 0 && nr < LIN && nc >= 0 && nc < COL)
            {
                if (map[nr, nc] == enemy)
                {
                    Unit? adj = units.Find(x => x.R == nr && x.C == nc && x.IsAlive && x.Type == enemy);
                    if (adj != null) lst.Add(adj);
                }
            }
        }
        return lst;
    }

    internal List<List<(int r, int c)>> GetAllMinPaths((int r, int c, int dist) chosenTarget, char[,] map, int LIN, int COL)
    {
        HashSet<(int r, int c)> seen = new();
        Queue<(int r, int c, int dist)> q = new();
        Dictionary<(int r, int c), (int level, HashSet<(int r, int c)> parents)> parents = new();

        q.Enqueue((R, C, 0));
        seen.Add((R, C));

        while (q.Count > 0)
        {
            (int r, int c, int dist) = q.Dequeue();

            if (chosenTarget == (r, c, dist))
                break;
            for (int i = 0; i < 4; i++)
            {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr >= 0 && nr < LIN && nc >= 0 && nc < COL)
                {
                    if (map[nr, nc] == '.' && !seen.Contains((nr, nc)))
                    {
                        seen.Add((nr, nc));
                        q.Enqueue((nr, nc, dist + 1));
                        parents[(nr, nc)] = (dist, new HashSet<(int r, int c)>() { (r, c) });
                    }
                    else if (map[nr, nc] == '.')
                        if (dist == parents[(nr, nc)].level)
                            parents[(nr, nc)].parents.Add((r, c));
                }
            }
        }


        return GetAllPaths(parents, (chosenTarget.r, chosenTarget.c));
    }

    private List<List<(int r, int c)>> GetAllPaths(Dictionary<(int r, int c), (int level, HashSet<(int r, int c)> parents)> parents, (int r, int c) current)
    {
        List<List<(int r, int c)>> result = new();
        if (parents.ContainsKey(current))
        {
            foreach (var item in parents[current].parents)
            {
                result.AddRange(GetAllPaths(parents, item));
            }
            foreach (var item in result)
                item.Add(current);
        }
        else
        {
            List<(int r, int c)> lst = new List<(int r, int c)>() { current };
            result.Add(lst);
        }
        return result;
    }

    internal HashSet<(int r, int c, int dist)> GetDistances(HashSet<(int r, int c)> reachable, char[,] map, int LIN, int COL)
    {
        HashSet<(int r, int c)> seen = new();
        HashSet<(int r, int c, int dist)> result = new();
        Queue<(int r, int c, int dist)> q = new();


        q.Enqueue((R, C, 0));
        seen.Add((R, C));

        while (q.Count > 0)
        {
            (int r, int c, int dist) = q.Dequeue();
            if (reachable.Contains((r, c)))
            {
                result.Add((r, c, dist));
            }

            for (int i = 0; i < 4; i++)
            {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr >= 0 && nr < LIN && nc >= 0 && nc < COL)
                {
                    if (map[nr, nc] == '.' && !seen.Contains((nr, nc)))
                    {
                        seen.Add((nr, nc));
                        q.Enqueue((nr, nc, dist + 1));
                    }
                }
            }
        }


        return result;
    }

    internal bool IsPathTo((int r, int c) x, char[,] map, int LIN, int COL)
    {
        Queue<(int r, int c)> q = new();
        HashSet<(int r, int c)> seen = new();
        q.Enqueue(x);
        seen.Add(x);

        while (q.Count > 0)
        {
            (int r, int c) = q.Dequeue();

            for (int k = 0; k < 4; k++)
            {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < LIN && nc >= 0 && nc < COL)
                {
                    if (nr == R && nc == C)
                        return true;
                    if (!seen.Contains((nr, nc)) && map[nr, nc] == '.')
                    {
                        q.Enqueue((nr, nc));
                        seen.Add((nr, nc));
                    }
                }
            }
        }
        return false;
    }
}
class ReadingOrder : IComparer<Unit>
{
    public int Compare(Unit? x, Unit? y)
    {
        if (x.R < y.R) return -1;
        else if (x.R > y.R) return 1;
        else if (x.C < y.C) return -1;
        else if (x.C > y.C) return 1;
        else return 0;
    }
}


internal class ReadingOrder<T> : IComparer<(int r, int c)>
{
    public int Compare((int r, int c) x, (int r, int c) y)
    {
        if (x.r < y.r) return -1;
        else if (x.r > y.r) return 1;
        else if (x.c < y.c) return -1;
        else if (x.c > y.c) return 1;
        else return 0;
    }
}

internal class ReadingDistanceComparer<T> : IComparer<(int r, int c, int dist)>
{
    public int Compare((int r, int c, int dist) x, (int r, int c, int dist) y)
    {
        if (x.r < y.r) return -1;
        else if (x.r > y.r) return 1;
        else if (x.c < y.c) return -1;
        else if (x.c > y.c) return 1;
        else return 0;
    }
}