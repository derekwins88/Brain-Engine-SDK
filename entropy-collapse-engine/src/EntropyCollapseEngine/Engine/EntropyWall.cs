namespace EntropyCollapseEngine.Engine;

public static class EntropyWall
{
    private const int NpWallStart = 5;
    private const int NpWallLen = 5;
    private const int NoRecoveryStart = 10;

    private const float NpWallThreshold = 0.09f;
    private const float NoRecoveryThreshold = 0.045f;

    public static EntropyWallResult Compute(float[] deltaPhi)
    {
        if (deltaPhi.Length < NoRecoveryStart)
            throw new ArgumentException(
                $"Expected at least {NoRecoveryStart} entropy points, got {deltaPhi.Length}",
                nameof(deltaPhi)
            );

        var npSlice = deltaPhi
            .Skip(NpWallStart)
            .Take(NpWallLen)
            .ToArray();

        var tailSlice = deltaPhi
            .Skip(NoRecoveryStart)
            .ToArray();

        var npWall = npSlice.Length == NpWallLen && npSlice.All(e => e > NpWallThreshold);
        var noRecovery = tailSlice.Length > 0 && tailSlice.All(e => e > NoRecoveryThreshold);

        return new EntropyWallResult
        {
            NpWall = npWall,
            NoRecovery = noRecovery,
            Series = deltaPhi.ToArray()
        };
    }
}
