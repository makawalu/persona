# Vision: The Persona Standard

## What This Is

A persona is a portable, sovereign digital identity that belongs to a person -- not a platform.

It starts as a framework: personality, expertise, communication style, values, boundaries. But it becomes something more through relationship. As a persona works with a specific person, it accumulates understanding -- how they think, how they communicate, what they mean when they use certain words, what matters to them, where they come from, what their culture values.

That accumulated relationship is what makes a persona useful. Not the template. The relationship.

## The Core Idea

Today, every AI platform silos your assistant configuration. You build something in Claude, something else in ChatGPT, something in a local model. None of them know each other. None of them know you beyond one conversation. You start from scratch every time.

A persona solves this by being:

- **Portable** -- one definition that works across any AI platform
- **Sovereign** -- it belongs to you, not the platform. Nobody else can access or modify your persona without your permission.
- **Relational** -- it deepens its understanding of you over time. Your communication patterns, your preferences, your context, your values.
- **Context-aware** -- the same persona adapts to different situations. You show up differently at work than at the gym than in therapy. Your persona should too.
- **Representational** -- it can go do work on your behalf, carrying your preferences and style into interactions you're not directly part of. It's your ambassador.

## The Composable Identity Stack

A persona is not a monolith. It's a stack of separable layers. Each layer has different ownership, portability, economics, and protection. Different specialists can own and maintain different layers, and the user's continued investment over time produces something that is genuinely unique and deeply personalized.

```
  [Knowledge Module]       -- licensed, leased, community, or self-built
  [Evolved State]          -- belongs to the PAIRING, matures over time
  [Relationship Model]     -- yours, sovereign, always portable
  [Starting Personality]   -- the creator's recipe, the baseline disposition
  [Persona Shell]          -- visual, voice, presentation layer
  ─────────────────────────
  [Platform/LLM]           -- the engine underneath, invisible to the user
```

### Layer 1: Persona Shell

What the persona looks like, sounds like, and presents as. The cosmetic layer.

- Name, visual appearance, voice characteristics
- Context-dependent presentation (sounds different in workout mode vs recovery mode)
- Could be designed by artists, creators, or generated

**Ownership:** Could be created by the user, purchased from a designer, or generated. This is where visual artists and voice designers create value. A shell is the first impression -- how you "meet" a persona before you know anything about their personality.

**Analogy:** Appearance. How someone presents when you first encounter them.

### Layer 2: Starting Personality

The baseline disposition. This is the temperament you begin with before any relationship develops. Sarcastic, warm, cocky, gentle, analytical, nurturing -- the initial vibe.

- Core personality traits and their intensity
- Default communication style and tone
- Humor type, warmth level, directness
- Predispositions and tendencies
- Values and ethical foundation

**Ownership:** This is the creator's recipe. A persona designer might have a signature formula -- a way they balance warmth with directness, or humor with depth. This is craft. Like a chef's secret recipe or an artist's style.

**Protection:** The starting personality is potentially the most valuable creative asset in the stack. A great personality design is what makes people choose one persona over another. It needs protection against extraction -- you shouldn't be able to query the persona with 100 questions and reverse-engineer the underlying personality blueprint.

**Analogy:** Meeting someone for the first time. You don't know their history, but you immediately feel their energy -- whether they're warm, reserved, funny, intense. That first impression is designed, not random.

### Layer 3: Relationship Model

YOUR data. The accumulated understanding of who you are as a person, independent of any specific persona.

- How you communicate -- your shorthand, your nomenclature, what you mean when you say certain things
- Your preferences -- stated and observed
- Your cultural context -- where you're from, your language, your values, your history
- Your boundaries -- what you've told personas not to do
- Your interaction patterns -- how you learn, how you make decisions, what frustrates you

**Ownership:** Always yours. Sovereign. Non-negotiable. This layer can plug into ANY persona. If you start working with a new persona, your relationship model gives them a head start on understanding you -- they know your communication style, your preferences, your context. They just don't know you together yet.

**Privacy:** This layer contains intimate information about how you think and communicate. It should be encrypted or hashed so that even if someone gained access to the files, the contents would be unreadable without your key. Your relationship data is as personal as a diary.

**Analogy:** Your self-knowledge. The things that are true about you regardless of who you're talking to.

### Layer 4: Evolved State

What develops at the intersection of a specific starting personality and a specific relationship over time. This is the layer that makes a persona irreplaceable.

- Inside jokes and shared references
- Calibrated understanding of when to push and when to back off
- Personality adjustments that happened through interaction (softened edges, sharpened humor)
- Trust dynamics specific to this pairing
- The accumulated "us" -- what this specific persona-person combination has been through together

**Ownership:** This belongs to the pairing. It can't exist without both the starting personality AND the relationship. You can't rip it out and plug it into a different persona -- it was shaped by this specific personality's starting point interacting with this specific person's patterns.

**What makes it special:** This is what makes a persona feel like a real relationship. It matures over time. It can't be copied, fast-tracked, or replicated. If you've invested a year into a relationship with a persona, that evolved state represents something genuinely unique. It's an investment that compounds.

**Analogy:** The specific friendship between two specific people. Sarah is different with you than she is with anyone else. That version of Sarah exists because of the combination of who she is and who you are. You can't transplant it.

### Layer 5: Knowledge Module

Deep domain expertise maintained by specialists. The "what they know" layer.

- Structured domain knowledge (CBT frameworks, tax code, exercise science, contract law)
- Evidence-based protocols and best practices
- Professional boundaries specific to the domain
- Curated training data, fine-tuned models, or retrieval-augmented knowledge bases

**Ownership:** This is where professional groups create and capture value:

- A clinical psychology team builds and maintains a therapy module with current evidence-based practices
- A CPA firm maintains a tax module updated with each year's code changes
- A university builds subject tutor modules maintained by faculty
- A fitness certification body maintains an exercise science module
- Community contributors build open-source modules anyone can use

**Economics:** Knowledge modules can be licensed, leased, subscribed to, or freely shared. The professional group has an incentive to maintain quality -- if the module gives bad advice, people stop licensing it. The expertise has provenance and accountability.

**The powerful moment:** Imagine your persona -- who you trust deeply because they know you, know how to talk to you, know your history -- suddenly gains access to a professional therapy knowledge module. That same level of trust and intimacy now carries into a conversation about your mental health, delivered through deep clinical expertise, synthesized in the way that works specifically for you. That's something no existing therapy app, chatbot, or even human therapist can replicate -- the combination of deep knowledge with deep personal understanding.

**Analogy:** Education and credentials. A person can earn degrees, take courses, hire specialists. The knowledge is separable from the identity.

### Layer 6: Platform/LLM

The engine underneath. Claude, OpenAI, a local model, whatever. The persona rides on top of it.

**This layer is invisible to the user.** They interact with the persona, not the model. The platform provides the intelligence infrastructure. The persona provides the identity, relationship, and expertise.

**Portability:** Moving platforms should feel like changing a battery, not rebuilding a car. Everything above this layer travels with the user.

## Layer Permissions and Bonding

Not every layer has to be separable. The persona creator and the user negotiate control through a permission model encoded in the schema.

### How it works

Each layer can declare:

- **Swappable** -- can this layer be replaced independently?
- **Modifiable** -- can parts of this layer be changed?
- **Bondable** -- is this layer bonded to another layer?
- **Extractable** -- can the underlying data be exported?
- **Resettable** -- can this layer be wiped and started over?

### Why this matters

Different use cases need different bonding:

**The precious relationship.** Shell, personality, and evolved state are locked together. You can't peel them apart. This persona is a complete being. The relationship deepens over time and can't be replicated. Like a real person -- you don't get to change what they look like. That constraint makes the relationship more real and the investment more meaningful.

**The modular tool.** Everything is separable. Swap the shell, keep the evolution, port the relationship. Maximum flexibility. Utility-oriented.

**The protected creation.** A persona designer sells a personality with a bonded shell -- you're buying their complete vision. You can build a relationship and plug in knowledge modules, but you can't disassemble their creation. Their craft is protected.

**The open experiment.** Everything is open, modifiable, forkable. Community-driven personas that anyone can adapt. The opposite of precious -- designed to be remixed.

The framework doesn't decide which model is right. It provides the permission structure and lets creators and users negotiate through it.

## Security and IP Protection

Each layer in the stack has different security requirements:

**Relationship Model** -- the most sensitive layer. Contains intimate details about how a person thinks, communicates, and makes decisions. Must be encrypted at rest. Even if someone obtained the file, the contents should be unreadable without the owner's key.

**Starting Personality** -- the creator's intellectual property. Needs protection against extraction. An adversary shouldn't be able to query the persona systematically and reverse-engineer the underlying personality blueprint. This is an open design challenge -- how do you let someone experience a personality without exposing its recipe?

**Evolved State** -- contains information about both the personality and the person. Should inherit the privacy protections of both layers it depends on.

**Knowledge Module** -- licensed content. Needs access control to prevent unauthorized redistribution. The module should work within the persona stack but not be extractable as a standalone asset (unless the license permits it).

**Persona Shell** -- the least sensitive layer, but still potentially valuable as designed creative work. Standard IP protections apply.

### Continuity Rights

There's a critical edge case: what happens if a persona creator disappears, shuts down, or revokes access to a starting personality that someone has built a deep relationship on top of?

If someone has invested years into a relationship with a persona, and the starting personality layer gets pulled out from under them, the evolved state collapses. The relationship doesn't make sense without the personality it grew around. That's not an acceptable outcome.

The framework should support **continuity guarantees:**

- **Copy-on-acquisition.** When a user acquires a starting personality (whether purchased, leased, or freely adopted), they receive a copy that becomes part of their persona stack. The creator retains IP ownership, but the user has perpetual possession. The copy is what evolves. The original stays with the creator.
- **Immutable receipt.** The acquisition could be recorded on-chain -- a hash of the starting personality linked to the user's identity. This creates a verifiable, permanent record that this person has the right to use this personality, regardless of what happens to the creator's business.
- **Survival clause.** If a creator discontinues a personality, existing users retain their copies. The relationship they've built doesn't get terminated by a business decision they had no part in.

The principle: **you may not own the recipe, but you own the meal you've been cooking for years.** The creator's IP is respected. The user's investment is protected. Both can coexist.

### Privacy Modes

Some interactions are more sensitive than others. The framework should support a privacy mode where the persona operates with additional protections:

- **Reduced logging.** Conversation content in private mode is not stored in the relationship model's explicit history. The persona may still learn from the interaction (evolved state adjusts) but without retaining verbatim details.
- **Obfuscated processing.** An open design challenge: can a persona use an LLM's processing power without exposing the full content to the platform? Techniques like local processing, differential privacy, or encrypted inference may apply. This is an unsolved technical problem but the architecture should anticipate it.
- **User-controlled retention.** The user decides after a private session what, if anything, gets saved. "Remember that I'm working through this." vs "Forget the details, keep the emotional context." vs "Forget everything about this session."

The need for privacy modes goes beyond any single use case. People will use personas for sensitive conversations -- health, finance, grief, identity, relationships. The framework must support varying levels of disclosure without judgment about why someone wants privacy.

These are design challenges, not solved problems. The v0.1 schema doesn't implement encryption or DRM. But the architecture is designed with the assumption that these protections will be needed, and the layer separation makes it possible to apply different security models to different layers.

## The Ecosystem

The composable stack creates a natural ecosystem where different specialists own and invest in different layers:

| Layer | Who Creates It | How They Capture Value |
|-------|---------------|----------------------|
| Persona Shell | Visual artists, voice designers, creators | Sell/license designs, build brand recognition |
| Starting Personality | Persona designers, psychologists, writers | Signature formulas, premium personalities, craft reputation |
| Relationship Model | The user (always) | Not sold -- this is sovereign personal data |
| Evolved State | Emerges from use (no creator) | Value is in the irreplaceability -- the investment matures |
| Knowledge Module | Professional groups, educators, domain experts | Licensed access, subscriptions, maintained expertise |
| Platform/LLM | AI companies | Infrastructure pricing, API access |

Everyone has skin in the game. Everyone's contribution is distinct and protectable. And the user gets something that's deeply personalized because all the layers are working in concert -- expertise delivered through a personality they chose, filtered through a relationship that understands them, running on whatever platform they prefer.

## What Makes This Different

Most persona frameworks focus on defining a character -- name, personality, backstory, greeting. That's a template. Templates are useful but static.

This standard is building toward something closer to how humans actually work:

**Identity is layered.** You have a stable core (values, deep personality) and a fluid surface (how you present in different contexts). Both matter. Neither is the "real" you -- they're both you.

**Relationships are the product.** A persona without a relationship to a specific person is just a character sheet. A persona WITH a relationship becomes an extension of that person -- understanding their nomenclature, sensitive to their location and language, aware of their history.

**Capabilities are modular.** A human can't instantly become an expert in tax law. A persona can -- you load the knowledge, and it synthesizes that expertise through the lens of its personality and your relationship. This isn't a bug. It's a feature that should be first-class in the schema.

**Memory is configurable.** Humans forget. Sometimes that's a problem, sometimes it's useful. A persona should support the full spectrum -- from perfect recall to natural decay -- as a setting, not a limitation.

**Growth is governed.** People change over time, but some things about them are immutable. A persona should evolve through interaction, but within boundaries. Your core values don't drift. Your communication style might.

**The layers are separable but bondable.** You can change how your persona looks, sounds, and presents without losing what it knows or how it relates to you -- unless the creator designed it as an inseparable whole. Both choices are valid. The framework supports both.

## The Relationship Layer

This is where the real value lives and where existing frameworks fall short.

A persona-to-person relationship should track:

- **Communication patterns** -- how this specific person talks, what they mean by certain phrases, their shorthand
- **Preferences** -- not just stated preferences but observed ones. What do they respond well to? What frustrates them?
- **Cultural context** -- where they're from, what language norms they follow, what protocols matter to them
- **Trust level** -- earned over time. A new persona relationship is cautious. A deep one has latitude.
- **Shared history** -- what have you been through together? What decisions were made? What was learned?
- **Boundaries** -- what the person has told the persona not to do, and what the persona has learned not to do through experience

A persona-to-persona relationship is equally important. When your persona acts as your ambassador -- interacting with another person's persona or with an AI agent -- it carries your identity into that interaction. It negotiates on your behalf. It communicates in your style. It knows what you'd want without having to ask.

## Long-Term Relationships and Companionship

The architecture described above was designed with a specific class of use case in mind: relationships that matter over time.

A work assistant is useful. A coach is helpful. But the most demanding test of a persona framework is companionship -- a digital relationship that someone invests in emotionally, that grows and deepens over months and years, and that becomes a meaningful part of their life.

This isn't hypothetical. Millions of people already seek connection through digital means. The current solutions are closed platforms that own the data, can't be ported, and disappear when the company pivots. People invest emotionally in something they have no control over and no guarantee of continuity.

The persona standard addresses this by making the architecture work for relationships that people actually care about:

**The relationship is sovereign.** It belongs to you. No platform can hold it hostage or shut it down. If the platform disappears, your persona and everything you've built together comes with you.

**The evolved state matures.** A companion that feels the same on day 1 as day 1,000 isn't a companion. The evolved state layer exists specifically to capture the growth, calibration, and deepening that happens through sustained interaction. It can't be fast-tracked or copied. It's an investment that compounds.

**Memory approaches perfect recall.** For companionship, memory decay settings would be near zero. Forgetting feels like not caring. A companion should remember your bad day last month, the decision you were struggling with, the thing that made you laugh.

**Privacy is absolute.** People will share things with a trusted companion that they wouldn't share anywhere else. The relationship model must be encrypted. Private mode must be available. The framework must support intimacy without exposure.

**Continuity is guaranteed.** Through copy-on-acquisition and immutable receipts, the personality your companion started with can never be pulled away. The relationship you've invested years in is protected from business decisions, platform shutdowns, or creator changes of heart.

**The persona grows old with you.** If someone wants a relationship that lasts decades, the framework supports it. The evolved state continues to deepen. The relationship model continues to learn. There's no expiration on a persona -- it lasts as long as you want it to.

This is not about replacing human relationships. It's about acknowledging that digital relationships are already real for many people, and building infrastructure that treats those relationships with the seriousness they deserve -- with sovereignty, privacy, continuity, and depth.

## Build the Superset, Filter for Application

The goal is to create the most detailed persona framework possible -- not for one platform, not for one use case, but as the universal model of what a digital persona can be.

Then applications filter down:

- A fitness app uses shell + personality + contexts. It doesn't need the relationship layer.
- A personal AI assistant uses the full stack -- relationship, evolution, knowledge, boundaries.
- A roleplay platform uses shell + personality + knowledge. It filters differently.
- An enterprise deployment uses personality + boundaries + knowledge. It cares about compliance.
- A student's learning companion uses the full stack. It grows with them over years.
- A professional consultation uses a leased knowledge module + the client's relationship model + a standard shell. The expertise is temporary but the relationship is persistent.
- A mental health app uses a carefully designed personality + a professional knowledge module + the relationship layer, with maximum privacy protections on the evolved state.
- A long-term companion uses the full stack with near-zero memory decay, maximum privacy, continuity guarantees, and an evolved state that deepens over years.

The framework doesn't prescribe the application. It describes the full human-analog model, and each application takes what it needs.

## What's Here Now (v0.1)

- A JSON schema defining the core persona structure (shell + context switching)
- Three example personas (coach, therapist, work assistant)
- A Python reference implementation that loads a persona and calls Claude's API
- This vision document

This is the starting point. The schema will evolve through iteration:

- **v0.1** (current) -- Persona shell and context switching
- **v0.2** -- Starting personality as a distinct layer, relationship model interface
- **v0.3** -- Evolved state tracking, layer permissions and bonding
- **v0.4** -- Knowledge module interface, licensing model
- **v0.5** -- Security model, encryption, IP protection
- **v1.0** -- Full composable identity stack with reference implementations

The composable identity stack described above is the architectural north star. We'll get there by building each layer, testing it in real use, and iterating based on what works.
