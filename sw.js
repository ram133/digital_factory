self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open("micropwa-v1").then((cache) => {
      return cache.addAll([
        "micro_pwa_template.html",
        "index.html"
      ]);
    })
  );
});

self.addEventListener("fetch", (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});
