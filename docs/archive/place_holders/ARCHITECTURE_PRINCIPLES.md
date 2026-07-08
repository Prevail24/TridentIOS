# TridentIOS Architecture Principles

## Principle 1

Models represent reality.

They never save themselves.

They never print themselves.

They never know about storage.

---

## Principle 2

Services coordinate.

They contain business logic.

---

## Principle 3

Storage persists.

It never contains business logic.

---

## Principle 4

Parsers translate.

They convert external representations into domain objects.

---

## Principle 5

Renderers present.

They decide how information is displayed.

They never know where data came from.

---

## Principle 6

Inside TridentIOS, everything is an object.

Files exist only at the edges of the system.