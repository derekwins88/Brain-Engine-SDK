using System.Text.Json.Serialization;

namespace EntropyCollapseEngine.Engine;

public sealed class EngineInput
{
    public List<float> DeltaPhi { get; set; } = new();
    public List<string> Motifs { get; set; } = new();

    public static EngineInput CreateSample()
    {
        return new EngineInput
        {
            DeltaPhi = new List<float>
            {
                0.00f, 0.01f, 0.02f, 0.03f, 0.04f,
                0.10f, 0.11f, 0.12f, 0.13f, 0.14f,
                0.06f, 0.05f, 0.05f, 0.05f, 0.05f,
                0.05f, 0.05f, 0.05f, 0.05f, 0.05f,
                0.05f
            },
            Motifs = new List<string> { "A", "B", "C", "A", "D" }
        };
    }
}

public sealed class ProofCapsule
{
    public string SchemaVersion { get; set; } = "capsule-1.1.0";
    public string Claim { get; set; } = "OPEN";

    public CapsuleMetadata Metadata { get; set; } = new();
    public float[] EntropySeries { get; set; } = Array.Empty<float>();
    public string[] Motifs { get; set; } = Array.Empty<string>();

    public string Cnf { get; set; } = string.Empty;
    public string Dimacs { get; set; } = string.Empty;

    public string Lean4Sketch { get; set; } = string.Empty;
}

public sealed class CapsuleMetadata
{
    [JsonPropertyName("pde_strength")]
    public double PdeStrength { get; set; }

    [JsonPropertyName("np_wall")]
    public bool NpWall { get; set; }

    [JsonPropertyName("no_recovery")]
    public bool NoRecovery { get; set; }

    [JsonPropertyName("sat_result")]
    public bool SatResult { get; set; }

    [JsonPropertyName("sat_provenance")]
    public SatProvenance SatProvenance { get; set; } = new();
}

public sealed class SatProvenance
{
    public string Mode { get; set; } = "stub";
    public string? Binary { get; set; } = null;
}

public sealed class EntropyWallResult
{
    public bool NpWall { get; init; }
    public bool NoRecovery { get; init; }
    public float[] Series { get; init; } = Array.Empty<float>();
}
