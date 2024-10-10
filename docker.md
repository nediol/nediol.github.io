---
title: Docker
layout: default
---

## Dockerfile Example

```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y nginx
CMD ["nginx", "-g", "daemon off;"]
```

<div class="button-container">
    <a href="/" class="button">Back to Main</a>
</div>
