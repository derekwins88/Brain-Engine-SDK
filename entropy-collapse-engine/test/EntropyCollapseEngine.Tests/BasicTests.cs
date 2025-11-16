using EntropyCollapseEngine.Engine;
using Xunit;

namespace EntropyCollapseEngine.Tests;

public class BasicTests
{
    [Fact]
    public void SampleRun_ProducesOpenClaim()
    {
        var input = EngineInput.CreateSample();
        var capsule = EntropyCollapseEngineCore.Run(
            input.DeltaPhi.ToArray(),
            input.Motifs.ToArray()
        );

        Assert.Equal("capsule-1.1.0", capsule.SchemaVersion);
        Assert.Equal("OPEN", capsule.Claim);
        Assert.NotEmpty(capsule.Cnf);
        Assert.NotEmpty(capsule.Dimacs);
    }
}
