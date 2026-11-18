# 彩星电影一号位 - 一键安装 (Windows PowerShell)
# 走 git clone，规避国内 raw.githubusercontent.com 不可达的问题
$ErrorActionPreference = "Stop"

$Repo = "https://github.com/SimonsTang/caixing-film-one.git"
$SkillDir = Join-Path $HOME ".workbuddy\skills\caixing-film-one"
$Tmp = Join-Path $env:TEMP ("caixing-install-" + [guid]::NewGuid().ToString("N"))

Write-Host "==> 彩星电影一号位 安装程序"
Write-Host "    目标目录: $SkillDir"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  Write-Error "需要 git，请先安装。"
  exit 1
}

git clone --depth 1 $Repo (Join-Path $Tmp "caixing-film-one")

$Parent = Split-Path $SkillDir
New-Item -ItemType Directory -Force -Path $Parent | Out-Null
if (Test-Path $SkillDir) {
  Write-Host "==> 检测到已安装，先备份旧版本"
  $bak = "${SkillDir}.bak." + (Get-Date -Format "yyyyMMddHHmmss")
  Move-Item -Path $SkillDir -Destination $bak
}
Move-Item -Path (Join-Path $Tmp "caixing-film-one") -Destination $SkillDir
$gitDir = Join-Path $SkillDir ".git"
if (Test-Path $gitDir) { Remove-Item -Path $gitDir -Recurse -Force }
Remove-Item -Path $Tmp -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "==> 安装完成: $SkillDir"
Write-Host "==> 请重启 WorkBuddy 会话后使用。"
