# Verificar una descarga de StoreAMO

StoreAMO publica un SHA-256 junto a cada APK oficial.

## Windows PowerShell

```powershell
Get-FileHash .\StoreAMO-0.4.3.87.apk -Algorithm SHA256
```

## Linux / Termux

```bash
sha256sum StoreAMO-0.4.3.87.apk
```

Compará el resultado con `SHA256SUMS.txt` del mismo GitHub Release.

No uses un hash copiado desde una fuente distinta al release oficial que contiene el APK.

## Fuente oficial

Los artefactos públicos de StoreAMO se distribuyen desde:

`https://github.com/desarrollamo/storeamo/releases`

Si el hash no coincide, no instales el archivo y reportalo por los canales publicados en `https://desarrollamo.com.ar/`.
