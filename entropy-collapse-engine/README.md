# Entropy Collapse Engine

This is a runnable C# console app that scaffolds the "entropy-collapse-engine" pipeline.

## Layout

```
entropy-collapse-engine/
  src/EntropyCollapseEngine/
  test/EntropyCollapseEngine.Tests/
  data/
  .github/workflows/
```

## Quickstart

```bash
dotnet new sln -n EntropyCollapseEngine
dotnet sln add src/EntropyCollapseEngine/EntropyCollapseEngine.csproj
dotnet sln add test/EntropyCollapseEngine.Tests/EntropyCollapseEngine.Tests.csproj

dotnet restore
dotnet build
dotnet test

dotnet run --project src/EntropyCollapseEngine --out out --in data/sample_input.json
```

The run produces `out/proof_capsule.json` using the sample data.
