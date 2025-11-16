namespace EntropyCollapseEngine.Engine;

public static class PdeFieldCalculator
{
    // Mimic the "Σ |clause| × 0.044" metric from your notes.
    public static double ComputePdeStrength(List<int[]> clauses)
    {
        var sum = 0.0;
        foreach (var clause in clauses)
        {
            sum += Math.Abs(clause.Length) * 0.044;
        }

        return sum;
    }
}
