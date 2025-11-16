namespace EntropyCollapseEngine.Engine;

public static class EntropyCollapseEngineCore
{
    public static ProofCapsule Run(float[] deltaPhi, string[] motifs)
    {
        var wall = EntropyWall.Compute(deltaPhi);
        var clauses = MotifClauseWeaver.FromMotifs(motifs);
        var cnf = MotifClauseWeaver.ToCnfString(clauses);
        var dimacs = MotifClauseWeaver.ToDimacs(clauses);

        var (isSat, satProv) = SatSolverStub.Run(clauses);
        var pde = PdeFieldCalculator.ComputePdeStrength(clauses);

        var claim = wall.NpWall && !isSat && wall.NoRecovery
            ? "P≠NP"
            : "OPEN";

        var leanSketch = Lean4SketchBuilder.BuildSketch(cnf, wall.NpWall, !isSat);

        return new ProofCapsule
        {
            SchemaVersion = "capsule-1.1.0",
            Claim = claim,
            Metadata = new CapsuleMetadata
            {
                PdeStrength = pde,
                NpWall = wall.NpWall,
                NoRecovery = wall.NoRecovery,
                SatResult = isSat,
                SatProvenance = satProv
            },
            EntropySeries = deltaPhi.ToArray(),
            Motifs = motifs.ToArray(),
            Cnf = cnf,
            Dimacs = dimacs,
            Lean4Sketch = leanSketch
        };
    }
}
