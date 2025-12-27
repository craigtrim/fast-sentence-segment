# poetry_download_model.ps1

# Full path of the file
$destination = 'resources/lib/en_core_web_sm-3.8.0.tar.gz'

#If the file does not exist, create it.
if (-not(Test-Path -Path $destination -PathType Leaf)) {
    try {
        $source = 'https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0.tar.gz'
        Invoke-WebRequest -Uri $source -OutFile $destination
        Write-Host "Model [$destination] has been downloaded."
    }
    catch {
        throw $_.Exception.Message
    }
}
# If the file already exists, show the message and do nothing.
else {
    Write-Host "Model [$destination] has already been downloaded."
}
