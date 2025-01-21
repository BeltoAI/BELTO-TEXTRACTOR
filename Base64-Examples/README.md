

```bash
echo "{\"filename\": \"SS-Pitch-D2D.pdf\", \"filedata\": \"$(base64 SS-Pitch-D2D.pdf)\"}" > request.json
```


```bash
curl -X POST http://127.0.0.1:5000/upload-base64 \
     -H "Content-Type: application/json" \
     --data @request.json
```
