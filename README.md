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

**3.** After my fix to the grounding prompt showed zero change in the
after-run, I asked Claude to help me figure out why instead of just
reporting "it didn't work." Given the before and after answers side by
side, it pointed out that my fix had targeted brevity-driven compression,
but the after-run disproved that theory — an instruction not to compress
had no measurable effect. Its alternative explanation was that the model
likely doesn't categorize "curved" as part of "exam format" at all. I
don't have an independent way to confirm that beyond what's already in
the two run logs, so I'm reporting it as the best explanation the
evidence supports, not a confirmed root cause.
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

Only criterion 1 was missed (3/5, every run). The other four were MET, so
this is one diagnosis, not five — but I also look below at whether some of
those four were too easy to begin with.

**Criterion 1 — generation stage, not retrieval.** Both misses are the same
subject: CS210 and MATH220 asking for exam format *and* workload in one
question. In both cases `store.py::search` retrieved the right chunk every
single run — `course_cs_210_exams.txt` and `course_math_220.txt` are in the
source list all three times for each question, and both chunks literally
contain the word "curved" (verified by reading the source files directly).
The chunk was never missing. What happened is in
`generate.py::answer_from_chunks`: the source sentence is "Two midterms and
a final, all drawn from lecture material... Midterms are curved, the final
is not." — the exam-count fact comes first, "curved" is a trailing clause
after it. In both questions, across all 6 runs (2 questions × 3 runs), the
model kept the first clause and dropped the second. The three questions
that *did* pass (laundry, add/drop, printing) don't have this shape — their
two needed facts are each a full, separate sentence, with nothing
competing for attention inside one sentence. So the real pattern isn't
"two-part questions are unreliable," it's narrower: a detail that's a
subordinate clause riding on a more prominent fact in the same sentence
gets summarized away when the question also asks for something else.
Retrieval and chunking did their job; the gap is in how the model
compresses the context into a sentence or two, per the "be brief" line in
`GROUNDING_INSTRUCTION`.

**Were any of the four MET criteria too easy?** Criterion 3 is the one I'd
point at. The gap between my in-corpus distances (0.2255–0.3936) and my
out-of-scope distances (0.825–0.934) is enormous — nothing in either group
comes anywhere near the 0.45 cutoff from either side. That means "4 of 5"
was never really at risk once the cutoff was set in that gap; this corpus
doesn't produce an ambiguous out-of-scope question the way a messier one
might. If I were tightening one target, it'd be this one — to 5 of 5, since
my actual data never came close to missing even one. Criterion 2, by
contrast, is genuinely being tested: source-naming is a model instruction
(`GROUNDING_INSTRUCTION`), not something the code forces, so 15/15 across
every run and question is a real result, not a guaranteed one.

## The Improvement

**What I changed:** Added one rule to `GROUNDING_INSTRUCTION` in
`generate.py`: "If the question asks about more than one thing, answer
every part of it. Do not drop a detail just because it's a secondary
clause in the source sentence rather than the main one." Also softened
"Be brief" to not override completeness.

**Why I picked it:** My diagnosis traced the criterion 1 miss to the
generation stage, not retrieval — the chunk containing "curved" was
retrieved every run for both failing questions, but the model's answer
never stated it. The fix targets that exact stage with a direct
instruction, rather than touching chunking or retrieval, which weren't
the problem.

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks state what their number refers to | 8 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 5. Multi-topic questions pull two docs | 3 of 5 | 3/5 | 3/5 | 3/5 | MET |

Produced by `run_eval.py::main`, `results/run_2026-09-30_1910_after.md`.
Real output, CS210 run 1, after the prompt change:

```
For CS 210, the assessment consists of two midterms and a final, all
drawn from lecture material rather than the textbook (sources:
`course_cs_210_exams.txt` and `course_cs_210.txt`). The workload is
front-loaded; the first month is heavier than the rest (source:
`course_cs_210_workload.txt`).
```

Still no "curved" — same gap as before the change, word for word in spirit.

**Did it help?** No. Before and after are identical: 3/5, 3/5, 3/5, same
two questions failing the same way, every run. The instruction change had
no measurable effect, which tells me my diagnosis had the right stage but
the wrong mechanism. I assumed the model was dropping "curved" under
space pressure from "be brief," so I told it not to do that — but telling
a model not to compress didn't change anything, which suggests it was
never compressing. More likely: the model doesn't categorize "curved" as
part of "exam *format*" at all — it reads "format" as midterms/final/
structure and treats grading curve as a different kind of fact, outside
what the question is asking about. That's not an instruction-following
problem, which is why an instruction didn't fix it — it's about which
facts the model considers responsive to the word "format" in the first
place, and that needs a differently-shaped fix than the one I tried.

## What's Still Broken

Criterion 1 is still missed after my one change — 3/5, 3/5, 3/5, identical
to before. Both failures are the same two questions (CS210, MATH220), and
the model still never states "curved," even though a retrieved chunk
contains it every single run.

What I'd do next: my fix assumed the model was dropping the detail under
space pressure from "be brief," and the after-run disproved that —
telling it not to compress had zero effect. The next thing worth trying
is a bigger change than a prompt line: a two-step generation, where the
model first lists every fact in the retrieved chunks relevant to the
question, then writes the answer from that list. That would force
"curved" to surface as a candidate fact instead of never being considered
at all. That's a real architecture change, not a one-line fix, and it
needs its own full test cycle to know if it works or just moves the
failure somewhere else.

Why I stopped where I did: time. Every iteration here costs a full
re-run — 15 real model calls minimum per cycle — and diagnosing *why* the
first fix failed, instead of assuming it worked, used the rest of my
budget for this unit. I'd rather report one fix honestly diagnosed as not
working than claim a second fix I didn't have time to test properly.

## What I'd Do Differently

The criterion I'd rewrite is criterion 1. As written, "the retrieved
chunks include one that contains the answer," and the thing my own
`scorer.py` actually checks (does the *final answer* contain the expected
phrase), turned out to be two different measurements — retrieval and
generation — and I only discovered that by manually reading the source
documents after the fact. Next unit I'd split it into two criteria from
the start: one strictly about retrieval (is the correct chunk in top-k,
checked against chunk text) and one about generation completeness (does
the final answer state every fact the retrieved chunks support). That
would have caught this miss accurately the first time instead of
requiring me to re-derive it by hand mid-unit.

Second, I'd tighten criterion 3. The gap between my in-corpus distances
(0.2255–0.3936) and out-of-scope distances (0.825–0.934) is enormous, so
"4 of 5" was never really being tested on this corpus. I'd set it to 5 of
5 next time, since nothing in my actual data came anywhere near the edge.
