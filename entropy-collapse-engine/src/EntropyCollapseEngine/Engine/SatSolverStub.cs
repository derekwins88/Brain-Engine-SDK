namespace EntropyCollapseEngine.Engine;

public static class SatSolverStub
{
    public static (bool isSat, SatProvenance provenance) Run(List<int[]> clauses)
    {
        // Simple stub:
        // - If any clause is empty, treat as UNSAT.
        // - Otherwise SAT.
        foreach (var c in clauses)
        {
            if (c.Length == 0)
            {
                return (false, new SatProvenance
                {
                    Mode = "stub-unit-contradiction",
                    Binary = null
                });
            }
        }

        return (true, new SatProvenance
        {
            Mode = "stub-sat",
            Binary = null
        });
    }
}
