# Caixing Film Director No.1

An all-in-one creative controller for Chinese-language comedy — screenwriter, producer, and director in one. The name is taken from the Choi Hing Film Company founded by Stephen Chow in 1994.

**Positioning**: This is not a Stephen Chow digital double. It does not impersonate, is not endorsed by, and does not reproduce protected expression from any person. It abstracts the underlying mechanics of Chow-style comedy into executable creative mechanisms, used to turn ordinary stories into content suited for cinemas, online streaming, and social media.

## Capabilities

- **Screenwriting**: character desire, status maps, rule conflicts, seven-beat structure, dialogue, prop payoff, emotional reversal.
- **Producing**: feasibility, budget scale, platform strategy, memorability engineering, rights and compliance.
- **Directing**: camera, performance, visual/verbal grading of jokes, comedy-to-tragedy triggers.
- **Innovation**: era-theme substitution, motif variation, medium-rhythm conversion, sharpness guardrails.
- **Distribution**: beat adaptation for shorts / mini-dramas / web films / cinema — hooks, completion rate, serialization.

## Install

Copy into the WorkBuddy user-level skills directory:

```bash
cp -r caixing-film-one ~/.workbuddy/skills/
```

Or use the one-click installer:

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/SimonsTang/caixing-film-one/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/SimonsTang/caixing-film-one/main/install.ps1 | iex
```

Restart the session to activate.

## Usage

```
Using caixing-film-one, turn "a temp worker who is always overlooked" into a 60-second original comedy with a visual conflict in the first 3 seconds.
```

```
Using caixing-film-one, diagnose why this scene isn't funny — give structural reasons first, then a minimal revision.
```

```
Using caixing-film-one, adapt the following story into a mini-drama for online streaming, keep the emotional core but don't copy any film.
```

**Safety words**: say "seriously" (认真) or "exit character" (退出角色) to switch back to neutral professional mode.

## Structure

```
caixing-film-one/
├── SKILL.md                          core workflow and routing
├── references/
│   ├── chow-playbook.md              distilled comedy mechanics matrix
│   ├── three-roles.md                screenwriter/producer/director decisions
│   ├── creation-workflows.md         workflows for each medium
│   ├── network-playbook.md           streaming and social media playbook
│   ├── evaluation-rubric.md          scoring rubric and hard failures
│   ├── rights-and-safety.md          originality and rights boundaries
│   └── source-registry.json          source registry
├── scripts/
│   ├── source_validator.py           source registry validation
│   ├── quote_guard.py                near-text checking
│   ├── evaluate_output.py            structure scoring
│   └── classic_score.py              classic-element coverage check
├── examples/sample-workflow.md       complete worked example
└── tests/validate_skill.py           structure validation
```

## Validation

```bash
python tests/validate_skill.py
python scripts/source_validator.py references/source-registry.json
python scripts/classic_score.py --input examples/sample-workflow.md
```

Scripts use only the Python standard library; 3.8+ recommended.

## Research and source boundaries

The methodology is distilled from long-form reviews on Douban, Rotten Tomatoes critic consensus, Wikipedia entries, and GitHub `stephen-chow-skill`. The research distinguishes verifiable facts, critical interpretation, and unverified rumors; it does not treat fabricated numbers from self-media as facts. See `references/source-registry.json` for the source list.

This project provides creative workflows and technical assistance, not legal advice. License: MIT (code and original documentation); no right is granted to any third party's name, likeness, voice, trademark, films, characters, screenplays, or dialogue.
