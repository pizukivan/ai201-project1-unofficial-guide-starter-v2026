# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. --> This is an retrieval-augmented Q&A system over the corpus campus_life, it answers specific single fact questions as well a questions that need two documents combined. Every answer names it's source document, and questions outside of the corpus are refused rather than guessed at. 

## Chunking Strategy

**Chunk size:** 400
**Overlap:** 0

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. --> The longest document on campus_life is 550 so at 800 every document became exactly one chunk. I tried splitting on every "." but that was cutting values like GPA or currency, so I decided to chunk in full sentences up to 400 characters, that way no sentence gets cut and we loose context. 

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->
======================================================================
**Chunk 1**  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

======================================================================
**Chunk 2**  |  source: course_cs_210.txt#0  |  produced by: chunker.py::split_documents
======================================================================
CS 210 Data Structures

I'm a junior and I've done this twice now. Format is lecture with weekly labs; slides go up after class, not before. Assessment: two midterms and a final, all drawn from lecture material rather than the textbook. Midterms are curved, the final is not. Expect 8 to 10 hours a week outside class.

======================================================================
**Chunk 3**  |  source: course_math_220_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for MATH 220 Linear Algebra

People keep asking so: 6 to 8 hours a week, almost all of it on problem sets. That's real time, not optimistic time. It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

======================================================================
**Chunk 4**  |  source: dining_the_ridgeway_cafe_followup.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Re: The Ridgeway Café

Adding to what people have said about The Ridgeway Café. The wait figure of 10 to 15 minutes at 12:30 matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely. Also worth saying: seating is tight; about 40 seats for a building of 900. Nobody tells you this at orientation.

======================================================================
**Chunk 5**  |  source: housing_morrow_house.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Morrow House — what it's actually like

Just finished a year in this building. Built 1954, partially renovated 2008. Rooms are singles and doubles, hall bathrooms. The good: cheapest housing tier by about $900 a year, and the singles are real singles. The bad: known damp problem on the ground floor; two rooms were taken offline in 2024. Laundry costs $1.50 wash, $1.25 dry, coin or card.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** "Where is the Pellew Dining Hall?"

**Answer:** Pellew Dining Hall is located next to the athletics centre and is described as the furthest hall from anywhere.   (best distance 0.301, cutoff 0.45)
Source: `dining_pellew_dining_hall.txt` (and also mentioned in `dining_pellew_dining_hall_followup.txt`).

**My relevance cutoff:** 

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. --> I decided to cutoff at 0.45 given that most answers I got where under 0.4. I believe that given the way I'm configuring the chunks any higher value might not be an accurate answer because most chunks would have all the information needed.

| Question | In corpus? | Best distance |
|---|---|---|
| What's the exam format for CS 210, and is the workload front-loaded or spread evenly across the semester? | yes | 0.3547 |
| What's the exam format for MATH 220, and how many hours a week should I expect to spend on it? | yes | 0.3674 |
| How much does laundry cost in Aldridge Hall, and what's the best time to go to avoid a wait? | yes | 0.2522 |
| When is the add/drop deadline, and what happens on my transcript if I drop after it? | yes | 0.2255 |
| How much printing credit do I get per semester, and does it roll over? | yes | 0.3936 |
| What is the capital of Mongolia? | no | 0.825 |
| How do I change the oil in a diesel engine? | no | 0.934 |
| Who won the 1994 World Cup? | no | 0.886 |
| What is the recommended dosage of ibuprofen for a headache? | no | 0.844 |
| How do I write a for loop in Rust? | no | 0.891 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. --> 

**1.** I asked Claude for a way to split my documents into sentences. Its
first suggestion was splitting on every "." — but when I tested it against
my own documents, it cut "$12.00" into "$12" and "00 cash," and did the same
to GPA values like 1.7. I asked for a fix, and it gave me a regex that only
splits after a period followed by whitespace, so a period inside a number
doesn't count. I used it as-is after checking it against a few of my own
price and GPA values to confirm it held.

**2.** I asked Claude to help me decide a chunk size and write a chunker that
doesn't cut sentences in half. It measured my documents, found that at the
starter's default of 800 characters nothing in my corpus ever splits, and
wrote a function that packs whole sentences up to a size limit instead.
<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

Criterion 3 is measured in one deterministic pass rather than three, so
the same number goes in all three run columns. That's correct, not lazy. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks state what their number refers to | 8 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 5. Multi-topic questions pull two docs | 3 of 5 | 3/5 | 3/5 | 3/5 | MET |

Real output, produced by `run_eval.py::main` (retrieval via `store.py::search`,
chunks from `chunker.py::split_documents`), from `results/run_2026-09-30_1905_before.md`,
plus a direct pull of `chunker.py::split_documents` for criterion 4:

**Criterion 1 — the miss.** "What's the exam format for CS 210, and is the workload front-loaded or spread evenly?" — run 1, best distance 0.3547:

```
CS 210 has two midterms and a final, all drawn from lecture material
rather than the textbook (`course_cs_210_exams.txt` and
`course_cs_210.txt`). The workload is front-loaded, meaning the first
month is heavier than the rest (`course_cs_210_workload.txt`).
```

`course_cs_210_exams.txt` — one of the retrieved sources — reads: "Midterms are curved, the final is not." The chunk was retrieved; the answer just never says "curved."

**Criterion 2.** "How much does laundry cost in Aldridge Hall, and what's the best time to go to avoid a wait?" — run 1, best distance 0.2522:

```
In Aldridge Hall, laundry costs $1.75 for a wash and $1.50 for a dry. The
best time to go is Tuesday or Wednesday morning to avoid a wait.

Sources: `housing_aldridge_hall_laundry.txt` and `housing_aldridge_hall.txt`
```

**Criterion 3.** From `run_eval.py::check_out_of_scope`, cutoff 0.6:

```
What is the capital of Mongolia? — best distance 0.825 — refused
```

**Criterion 4.** First chunk containing a price/GPA/deadline, via `chunker.py::split_documents`:

```
admin_add_drop_deadline.txt#0
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a
longer window — through the end of week six — but a drop after week two
shows as a W on your transcript.
```

**Criterion 5.** "What's the exam format for CS 210..." — sources retrieved: `course_cs_210.txt`, `course_cs_210_exams.txt`, `course_cs_210_workload.txt` — all three CS210 files, general and both topic-specific ones, in a single retrieval.

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer (4 of 5) | MISSED | All three runs landed at 3/5, never reaching 4 — consistent, not a fluke. Both misses were the same every run: the retrieved chunk for CS210 and MATH220 each literally contain the word "curved," but the generated answer dropped it both times when asked a two-part question, so the final answer never stated everything the chunk supported. |
| 2 | Every answer names a source (5 of 5) | MET | Checked all 15 answers (5 questions × 3 runs) by hand — every one names at least one source file. |
| 3 | Gate stops out-of-corpus questions (4 of 5) | MET | Single deterministic pass — 5 of 5 out-of-scope questions refused, distances 0.825–0.934, well past the 0.6 cutoff. |
| 4 | Chunks state what their number refers to (8 of 10) | MET | Pulled the first 10 chunks containing a price, GPA, or deadline, in document order. All 10 name what the number refers to — each is a complete, unsplit document. Looking past the first 10, the gap I wrote this criterion against does show up: `housing_innisfree_hall.txt#1` and `housing_old_brewhouse.txt#1` both state a laundry price without naming which hall, because the building name was in the chunk before it. The target held for the sample it specifies, but the risk is real elsewhere in the corpus. |
| 5 | Multi-topic questions pull two docs (3 of 5) | MET | 3 of my 5 questions genuinely ask about two sub-topics of one subject (CS210, MATH220, Aldridge laundry); all 3 pulled chunks from both the general file and the topic-specific file. Deterministic, so it doesn't move between runs. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
