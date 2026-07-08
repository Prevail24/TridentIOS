from core.services.entity_resolver import EntityResolver

resolver = EntityResolver()

a = resolver.resolve("domain", "Acme.COM")
b = resolver.resolve("domain", "acme.com")

print(a.id)
print(b.id)
print(a.id == b.id)