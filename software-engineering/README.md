# Software Engineering

Everything that isn't DSA and isn't behavioral: system design, CS fundamentals,
language-specific questions, and web.

## What each level is tested on

The loop looks similar at every level — the difference is what each round is
weighted at and what a passing answer looks like. Titles vary by company; the
progression doesn't.

| | Intern | New grad | Mid (L4) | Senior (L5) | Staff+ (L6+) |
|---|---|---|---|---|---|
| **Coding / DSA** | Nearly all of it | Most of it | Still the core | One or two rounds | Often one, sometimes none |
| **System design** | — | Rare, junior-scoped | One round | **Highest weight** | **Highest weight**, plus architecture depth |
| **CS fundamentals** | Heavy | Heavy | Moderate | Light, but assumed | Assumed |
| **Behavioral** | Coachability | Coachability | Ownership | Scope and influence | Org-level impact |
| **What they're buying** | Potential | Potential | Independent execution | Judgment | Leverage on other people's work |

### Intern and new grad

Almost entirely algorithmic. You're judged on whether you can write correct code
under time pressure and explain your reasoning — not on production experience
you haven't had yet. CS fundamentals get asked directly here in a way they
mostly stop being asked later: OS, networks, and databases show up as recall
questions rather than as assumptions baked into a design discussion.

Spend your time in [../dsa/](../dsa/) and [cs-fundamentals/](cs-fundamentals/).
Skip system design unless a specific company tells you it's in the loop; when it
does appear at this level it's scoped down to something like "design a URL
shortener" with a much lower bar.

Behavioral is about coachability and interest, not war stories. Class projects,
internships, and open source are legitimate material.

### Mid-level

DSA is still the core of the loop and the most common reason people fail. What
changes is that one system design round appears and is real, and behavioral
shifts from potential to evidence — they want to hear that you owned something
end to end and dealt with the consequences.

The design round at this level rewards a complete, working, unsurprising answer.
You're not expected to invent a novel architecture; you're expected to reach a
sane one, know why each piece is there, and not leave the data model vague.

### Senior

System design becomes the highest-variance round and usually the one that
decides the outcome. Work through [system-design/](system-design/) first and
give it the most time.

The bar moves from "does it work" to **judgment**: you're expected to drive the
conversation, surface constraints the interviewer didn't state, name tradeoffs
explicitly, and pick one with a reason. Saying "I'd use Kafka here" is a
mid-level answer. Saying what you gain, what it costs you operationally, and
what you'd use instead if the team were three people is a senior one.

DSA still appears and still eliminates people — plenty of strong senior
candidates fail on a medium they hadn't practiced in years. Keep it warm, but it
is no longer where your marginal hour pays best.

Behavioral becomes scope and influence: projects spanning multiple people or
teams, disagreements you resolved, things you shipped that were the wrong call.

### Staff and above

Everything senior-level, plus a shift from designing one system to reasoning
about how systems and teams interact. Expect architecture rounds with
deliberately underspecified problems, where the first real test is what you ask
before designing anything.

Common additions: deep dives on a past project where the interviewer pushes
until they find the edge of your knowledge; technical strategy questions with no
clean answer; and behavioral rounds about influence without authority,
mentorship, and decisions you drove across an org.

Coding is often reduced to a single pragmatic round, occasionally dropped
entirely. Don't read that as "no coding" until the recruiter confirms it —
policies differ per company and per team.

### What to do with this

The routes in the [root README](../README.md) assume the mid-to-senior shape.
Adjust the proportions: earlier career, push time into [../dsa/](../dsa/) and
[cs-fundamentals/](cs-fundamentals/); later career, push it into
[system-design/](system-design/) and [../behavioral/](../behavioral/).

Ask your recruiter what the loop actually contains. They will usually tell you
the round breakdown, and it beats guessing from a table.

## Contents

| Folder | What's in it |
|---|---|
| [system-design/](system-design/) | Design-round framework, template, curated reference list |
| [cs-fundamentals/](cs-fundamentals/) | OS, networks, databases, OOP, computer architecture, SWE practice |
| [languages/](languages/) | Java, JavaScript, Python question sets |
| [web/](web/) | Web/frontend fundamentals |

## system-design/

- `README.md` — the primer: how to run a design interview, engineering blogs,
  system/product breakdowns, hot questions with references, OOD tips
- `system-design-template.docx` — the structure to follow live: constraints →
  use cases → high-level architecture → component design → scale

## cs-fundamentals/

| Topic | Contents |
|---|---|
| `operating-systems/` | Notes, interview questions, Modern Operating Systems 3e + solutions, links |
| `computer-networks/` | Notes, links |
| `databases/` | DBMS interview questions, DBMS notes, links |
| `object-oriented-programming/` | Notes, top-50 OOP question set |
| `computer-architecture/` | Notes |
| `software-engineering-fundamentals/` | SDLC, methodology, practice |

## languages/

- `java/` — Java interview questions
- `javascript/` — JavaScript interview questions
- `python/` — decorators, slicing

## web/

- `virtual-dom.docx`

## How to use this route

Weight the folders by the level you're targeting — see
[what each level is tested on](#what-each-level-is-tested-on) above.
`cs-fundamentals/` is mostly recall and rewards spaced review over long
sessions; keep the `links.txt` files, they point at sources better than the
PDFs. Hit `languages/` only for the stack the role actually uses.
