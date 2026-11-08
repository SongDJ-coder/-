# Obsidian 노트(C:\Obsidian\DeepLearning)를 레포의 notes\ 폴더로 복사한다.
# 사용법: C:\Deeplerning 에서  .\sync_notes.ps1
# /MIR: 원본과 똑같이 맞춘다 (원본에서 지운 파일은 notes\에서도 지워짐)
$src = "C:\Obsidian\DeepLearning"
$dst = Join-Path $PSScriptRoot "notes"
robocopy $src $dst /MIR /XD .obsidian /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { Write-Error "복사 실패 (robocopy 코드 $LASTEXITCODE)"; exit 1 }
Write-Host "노트 동기화 완료: $src -> $dst"
