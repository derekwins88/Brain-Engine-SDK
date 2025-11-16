namespace EntropyCollapseEngine.Engine;

public static class MotifClauseWeaver
{
    // Simple placeholder mapping; you can later externalize this.
    private static readonly Dictionary<string, int> MotifVars = new()
    {
        ["A"] = 1,
        ["B"] = 2,
        ["C"] = 3,
        ["D"] = 4,
        ["E"] = 5
    };

    public static List<int[]> FromMotifs(string[] motifs)
    {
        var clauses = new List<int[]>();

        for (var i = 0; i < motifs.Length - 1; i++)
        {
            var m1 = motifs[i];
            var m2 = motifs[i + 1];

            if (!MotifVars.TryGetValue(m1, out var v1)) continue;
            if (!MotifVars.TryGetValue(m2, out var v2)) continue;

            // Example clause: (m1 ∨ ¬m2)
            clauses.Add(new[] { v1, -v2 });
        }

        if (clauses.Count == 0)
        {
            // Guarantee at least one clause so downstream SAT isn't degenerate
            clauses.Add(new[] { 1, -1 });
        }

        return clauses;
    }

    public static string ToCnfString(List<int[]> clauses)
    {
        var parts = new List<string>();
        foreach (var c in clauses)
        {
            var lits = c.Select(l => (l > 0 ? "" : "¬") + "x" + Math.Abs(l));
            parts.Add("(" + string.Join(" ∨ ", lits) + ")");
        }

        return string.Join(" ∧ ", parts);
    }

    public static string ToDimacs(List<int[]> clauses)
    {
        var (numVars, numClauses) = GetStats(clauses);
        var lines = new List<string> { $"p cnf {numVars} {numClauses}" };

        foreach (var clause in clauses)
        {
            lines.Add(string.Join(" ", clause.Select(l => l.ToString())) + " 0");
        }

        return string.Join(Environment.NewLine, lines) + Environment.NewLine;
    }

    private static (int numVars, int numClauses) GetStats(List<int[]> clauses)
    {
        var numVars = 0;
        foreach (var clause in clauses)
        {
            foreach (var lit in clause)
            {
                numVars = Math.Max(numVars, Math.Abs(lit));
            }
        }

        return (numVars, clauses.Count);
    }
}
