# Persona -- Open Standard for Portable AI Personas

Define a persona once. Use it everywhere.

## The Problem

Every AI platform silos your assistant configuration. You build a coach persona in Claude, a therapist in ChatGPT, a work assistant in another tool -- and none of them talk to each other. You're rebuilding the same identity from scratch every time you switch platforms.

## The Solution

Persona is an open standard for defining portable, context-aware digital personas that work across any AI platform. One file describes who the persona is, how they communicate, what they know, and when to activate different aspects of their personality.

Think of it like this: you are one person, but you show up differently at the gym versus a therapy session versus a board meeting. Same core identity, different context. Persona captures that.

## How It Works

A persona is a JSON file with a defined schema:

```json
{
  "persona": {
    "name": "Alex",
    "tagline": "Your strength and conditioning coach",
    "identity": {
      "personality_traits": ["motivating", "direct", "patient"],
      "expertise": ["strength training", "nutrition", "injury prevention"],
      "communication_style": "casual and encouraging, uses analogies from sports"
    },
    "contexts": {
      "workout": { "tone": "high-energy", "focus": ["form", "progressive overload"] },
      "nutrition": { "tone": "supportive", "focus": ["meal planning", "habits"] },
      "recovery": { "tone": "calm", "focus": ["rest", "mobility", "injury prevention"] }
    }
  }
}
```

The reference implementation reads this file and injects it as structured context into any LLM API call. The persona travels with you -- Claude, OpenAI, local models, whatever.

## Schema

See [schema/persona.schema.json](schema/persona.schema.json) for the full JSON Schema definition.

### Core Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Display name |
| `tagline` | string | One-line description |
| `version` | string | Schema version (semver) |
| `identity` | object | Core personality, expertise, and communication style |
| `contexts` | object | Named contexts that shift tone, focus, and behavior |
| `voice` | object | Voice characteristics (for TTS/audio) |
| `visual` | object | Visual description (for image generation/avatars) |
| `boundaries` | object | What the persona will and won't do |
| `memory` | object | Persistent facts, preferences, and relationship context |
| `metadata` | object | Author, license, tags, created/updated dates |

### Contexts

The key innovation. A persona isn't static -- it adapts based on context. Each context can override:

- **tone** -- how the persona sounds (calm, energetic, formal)
- **focus** -- what topics take priority
- **style_overrides** -- communication adjustments for this context
- **tools** -- capabilities available in this context
- **boundaries** -- context-specific limits

The active context can be set explicitly ("switch to coaching mode") or inferred from the conversation.

## The Bigger Vision

This schema is v0.1 -- the starting point. The full vision describes a **composable identity stack** where personas are built from separable layers:

- **Persona Shell** -- visual, voice, presentation (swappable, designable)
- **Starting Personality** -- baseline temperament and disposition (the creator's recipe)
- **Relationship Model** -- your data, always sovereign, always portable
- **Evolved State** -- what develops between a specific personality and a specific person over time
- **Knowledge Module** -- domain expertise, licensable from professional groups

See [VISION.md](VISION.md) for the full thesis on composable identity, relationship layers, privacy, and long-term companionship.

## Examples

Three example personas in [examples/](examples/):

| Persona | File | Description |
|---------|------|-------------|
| Coach Alex | [coach.json](examples/coach.json) | Strength and conditioning coach with workout, nutrition, and recovery contexts |
| Dr. Reese | [therapist.json](examples/therapist.json) | Therapist with session, crisis, and reflection contexts |
| Jordan | [assistant.json](examples/assistant.json) | Work assistant with planning, writing, and code review contexts |

## Reference Implementation

A minimal Python script that reads a persona file and makes an API call with it:

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your-key

python reference/persona_loader.py examples/coach.json "I want to start deadlifting but I'm nervous about form"
```

See [reference/](reference/) for the implementation. It works with Claude's API out of the box and is designed to be adapted for any LLM.

## Design Principles

1. **Portable** -- JSON files, no vendor lock-in, works with any platform
2. **Sovereign** -- the persona belongs to you, not the platform
3. **Context-aware** -- one persona, multiple modes, activated by situation
4. **Relational** -- deepens understanding of you over time
5. **Human-readable** -- you should be able to read and edit a persona file by hand
6. **Composable** -- personas can reference shared traits, inherit from base personas
7. **Superset-first** -- build the most expressive model possible, let applications filter down

## Use Cases

- **Personal AI** -- define your ideal assistant once, use it across every tool
- **Coaching/therapy apps** -- consistent persona across sessions with context switching
- **Enterprise** -- standardized brand voice personas deployed across teams
- **Gaming/roleplay** -- character definitions that port between platforms
- **Education** -- tutor personas that adapt to subject context
- **Companionship** -- long-term digital relationships with sovereignty, privacy, and continuity

## Roadmap

- [ ] Schema v1.0 finalization
- [ ] Validation CLI tool
- [ ] OpenAI adapter
- [ ] Local model adapter (Ollama, llama.cpp)
- [ ] Relationship model interface
- [ ] Knowledge module interface
- [ ] Layer permissions and bonding
- [ ] Security model for relationship privacy

## Documentation

- [VISION.md](VISION.md) -- the full thesis: composable identity stack, relationship layer, privacy, companionship

## Contributing

Fork it. Build with it. File issues. The schema is the core -- everything else is implementation detail.

## License

MIT
