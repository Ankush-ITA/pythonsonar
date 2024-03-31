Start-Transcript -Path $logFilePath -Append

function Log-Message {
    param (
        [string]$message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] $message"
    $message | Out-File -Append -FilePath $logFilePath
}

Write-Host "$user exists in the group  so removing now from the group"

Log-Message "$user exists in the group  so removing now from the group."
Remove-ADGroupMember -Identity $group -Members $user -Confirm:$false

Stop-Transcript
