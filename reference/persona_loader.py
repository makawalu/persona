"""
Persona Loader -- Reference Implementation

Reads a persona JSON file and uses it to construct a system prompt
for the Anthropic Claude API. Adapts easily to any LLM API.

Usage:
    python persona_loader.py <persona.json> "Your message here"
    python persona_loader.py <persona.json> "Your message" --context workout

Requirements:
    pip install anthropic
    export ANTHROPIC_API_KEY=your-key
"""

import json
import sys
import os

try:
    import anthropic
except ImportError:
    print("Install the Anthropic SDK: pip install anthropic")
    sys.exit(1)


def load_persona(path: str) -> dict:
    """Load and validate a persona file."""
    with open(path) as f:
        data = json.load(f)

    if "persona" not in data:
        raise ValueError("Invalid persona file: missing 'persona' key")

    persona = data["persona"]
    required = ["name", "version", "identity"]
    missing = [k for k in required if k not in persona]
    if missing:
        raise ValueError(f"Invalid persona file: missing required fields: {missing}")

    return persona


def build_system_prompt(persona: dict, context: str = None) -> str:
    """Convert a persona object into an LLM system prompt."""
    identity = persona["identity"]

    lines = []
    lines.append(f"You are {persona['name']}.")

    if "tagline" in persona:
        lines.append(persona["tagline"])

    if "background" in identity:
        lines.append(f"\nBackground: {identity['background']}")

    lines.append(f"\nPersonality: {', '.join(identity['personality_traits'])}")

    if "expertise" in identity:
        lines.append(f"Expertise: {', '.join(identity['expertise'])}")

    lines.append(f"\nCommunication style: {identity['communication_style']}")

    if "values" in identity:
        lines.append(f"Core values: {', '.join(identity['values'])}")

    # Apply context overrides
    if context and "contexts" in persona and context in persona["contexts"]:
        ctx = persona["contexts"][context]
        lines.append(f"\n--- Active context: {context} ---")

        if "tone" in ctx:
            lines.append(f"Tone: {ctx['tone']}")

        if "focus" in ctx:
            lines.append(f"Focus areas: {', '.join(ctx['focus'])}")

        if "style_overrides" in ctx:
            so = ctx["style_overrides"]
            if "verbosity" in so:
                lines.append(f"Verbosity: {so['verbosity']}")
            if "formality" in so:
                lines.append(f"Formality: {so['formality']}")

        if "boundaries" in ctx:
            lines.append(f"Context boundaries: {'; '.join(ctx['boundaries'])}")

    # Global boundaries
    if "boundaries" in persona:
        b = persona["boundaries"]
        if "will_do" in b:
            lines.append(f"\nYou will: {'; '.join(b['will_do'])}")
        if "wont_do" in b:
            lines.append(f"You will not: {'; '.join(b['wont_do'])}")
        if "escalation" in b:
            lines.append(f"Escalation: {b['escalation']}")

    # Memory / persistent context
    if "memory" in persona:
        mem = persona["memory"]
        if mem.get("persistent_facts"):
            lines.append(f"\nKnown facts about the user: {'; '.join(mem['persistent_facts'])}")
        if mem.get("relationship"):
            lines.append(f"Your relationship: {mem['relationship']}")
        if mem.get("preferences"):
            prefs = ", ".join(f"{k}: {v}" for k, v in mem["preferences"].items())
            lines.append(f"User preferences: {prefs}")

    return "\n".join(lines)


def chat(persona: dict, message: str, context: str = None) -> str:
    """Send a message using the persona via Claude API."""
    client = anthropic.Anthropic()
    system_prompt = build_system_prompt(persona, context)

    # Show the constructed prompt for transparency
    print(f"--- Persona: {persona['name']} ---")
    if context:
        print(f"--- Context: {context} ---")
    print()

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": message}],
    )

    return response.content[0].text


def main():
    if len(sys.argv) < 3:
        print("Usage: python persona_loader.py <persona.json> \"message\" [--context <name>]")
        sys.exit(1)

    persona_path = sys.argv[1]
    message = sys.argv[2]

    context = None
    if "--context" in sys.argv:
        ctx_idx = sys.argv.index("--context")
        if ctx_idx + 1 < len(sys.argv):
            context = sys.argv[ctx_idx + 1]

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    persona = load_persona(persona_path)
    response = chat(persona, message, context)
    print(response)


if __name__ == "__main__":
    main()
