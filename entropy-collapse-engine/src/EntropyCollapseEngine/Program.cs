using System.Text.Json;
using System.Text.Json.Serialization;
using EntropyCollapseEngine.Engine;

namespace EntropyCollapseEngine;

public static class Program
{
    public static int Main(string[] args)
    {
        try
        {
            var options = ParseArgs(args);
            Directory.CreateDirectory(options.OutDirectory);

            EngineInput input;
            if (options.InputFile is null)
            {
                Console.WriteLine("No --in provided, using built-in sample input.");
                input = EngineInput.CreateSample();
            }
            else
            {
                var json = File.ReadAllText(options.InputFile);
                input = JsonSerializer.Deserialize<EngineInput>(json)
                         ?? throw new InvalidOperationException("Failed to parse input JSON.");
            }

            var capsule = EntropyCollapseEngineCore.Run(
                input.DeltaPhi.ToArray(),
                input.Motifs.ToArray()
            );

            var capsuleJson = JsonSerializer.Serialize(
                capsule,
                new JsonSerializerOptions
                {
                    WriteIndented = true,
                    DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull
                }
            );

            var outPath = Path.Combine(options.OutDirectory, "proof_capsule.json");
            File.WriteAllText(outPath, capsuleJson);
            Console.WriteLine($"Wrote capsule to {outPath}");

            return 0;
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine("Error: " + ex);
            return 1;
        }
    }

    private static EngineOptions ParseArgs(string[] args)
    {
        string? inputFile = null;
        var outDir = "out";

        for (var i = 0; i < args.Length; i++)
        {
            switch (args[i])
            {
                case "--in":
                    if (i + 1 >= args.Length) throw new ArgumentException("--in requires a path");
                    inputFile = args[++i];
                    break;
                case "--out":
                    if (i + 1 >= args.Length) throw new ArgumentException("--out requires a path");
                    outDir = args[++i];
                    break;
            }
        }

        return new EngineOptions(inputFile, outDir);
    }

    private sealed record EngineOptions(string? InputFile, string OutDirectory);
}
