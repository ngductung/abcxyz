```cmd
powershell -Command "(netsh wlan show profiles) | Select-String ':(.+)$' | ForEach-Object {$name=$_.Matches.Groups[1].Value.Trim(); $_} | ForEach-Object {(netsh wlan show profile name=\"$name\" key=clear)} | Select-String 'Key Content\s+:\s+(.+)$' | ForEach-Object {$pass=$_.Matches.Groups[1].Value.Trim(); $_} | ForEach-Object {[PSCustomObject]@{PROFILE_NAME=$name;PASSWORD=$pass}} | Format-Table -AutoSize"

```

```powershell
(netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)}  | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{ PROFILE_NAME=$name;PASSWORD=$pass }} | Format-Table -AutoSize

```

```bash
sudo grep -h "^id\|psk=" /etc/NetworkManager/system-connections/* | tr "=" " " | cut -d " " -f2 | sed '$!N;s/\n/:/'
```
