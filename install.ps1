# 彩星电影一号位 - 一键安装 (Windows PowerShell)
$ErrorActionPreference = "Stop"

$RepoRaw = "https://raw.githubusercontent.com/SimonsTang/caixing-film-one/main"
$SkillDir = Join-Path $HOME ".workbuddy\skills\caixing-film-one"
$Tmp = Join-Path $env:TEMP ("caixing-install-" + [guid]::NewGuid().ToString("N"))

Write-Host "==> 彩星电影一号位 安装程序"
Write-Host "    目标目录: $SkillDir"

New-Item -ItemType Directory -Force -Path $Tmp | Out-Null
$Files = @(
  "SKILL.md", "README.md", "README.en.md", "LICENSE",
  "references/chow-playbook.md",
  "references/three-roles.md",
  "references/creation-workflows.md",
  "references/network-playbook.md",
  "references/evaluation-rubric.md",
  "references/rights-and-safety.md",
  "references/source-registry.json",
  "scripts/source_validator.py",
  "scripts/quote_guard.py",
  "scripts/evaluate_output.py",
  "scripts/classic_score.py",
  "examples/sample-workflow.md",
  "tests/validate_skill.py"
)
foreach ($f in $Files) {
  $dest = Join-Path $Tmp ("caixing-film-one\" + ($f -replace "/", "\"))
  New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
  Invoke-WebRequest -Uri "$RepoRaw/$f" -OutFile $dest -UseBasicParsing
}

$Parent = Split-Path $SkillDir
New-Item -ItemType Directory -Force -Path $Parent | Out-Null
if (Test-Path $SkillDir) {
  Write-Host "==> 检测到已安装，先备份旧版本"
  $bak = "${SkillDir}.bak." + (Get-Date -Format "yyyyMMddHHmmss")
  Move-Item -Path $SkillDir -Destination $bak
}
Move-Item -Path (Join-Path $Tmp "caixing-film-one") -Destination $SkillDir
Remove-Item -Path $Tmp -Recurse -Force

Write-Host "==> 安装完成: $SkillDir"
Write-Host "==> 请重启 WorkBuddy 会话后使用。"
