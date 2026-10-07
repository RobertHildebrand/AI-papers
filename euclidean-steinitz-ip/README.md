# Euclidean Steinitz Bounds for Graver Bases and Integer Programming

An AI-generated working draft prepared for Robert Hildebrand, October 7, 2026.

- [Read the paper (PDF)](main.pdf)
- [Edit the self-contained LaTeX source](main.tex)

The bibliography is embedded in `main.tex`; no external bibliography or figure files are required.

## Citation

Suggested title-led citation for this dated draft ([download BibTeX](citation.bib)):

```bibtex
@misc{AIpapers:EuclideanSteinitzIP:2026,
  key          = {Euclidean Steinitz Bounds},
  title        = {{Euclidean Steinitz Bounds for Graver Bases and Integer Programming: Conditional structural bounds and algorithmic consequences}},
  howpublished = {AI-papers repository preprint},
  year         = {2026},
  month        = oct,
  url          = {https://github.com/RobertHildebrand/AI-papers/tree/main/euclidean-steinitz-ip},
  note         = {AI-generated working draft prepared for Robert Hildebrand, dated October 7, 2026}
}
```

For the exact version you use, replace `main` in the URL with its full Git commit identifier and add the identifier to the `note`. See the repository’s [version and attribution guidance](../README.md#versions-and-citations).

## Mathematical scope

The paper develops consequences of the Euclidean rearrangement bound claimed in the September 24, 2026 OpenAI math preprint release. The geometric input is explicitly an assumption: this draft does not independently verify the released analytic proof.

Complete arguments are supplied for:

- A Graver bound in the maximum Euclidean column norm: `g_1(A) <= [K(1+D)]^m`.
- LP–IP proximity with integral lower and upper variable bounds, including a proof that handles fractional coordinates through translated lattice cosets.
- A bounded-variable dynamic program, a separable-convex improvement oracle, and a standard-form tube graph with explicit state and operation counts.
- A two-level block-matrix bound: `g_1(H) <= G Q_r(D_A G)`, where `G = Q_s(D_B)` or a supplied sharper local Graver bound.
- A sparse chain lower bound and an unconditional comparison using classical Steinitz in the l1 norm.
- A balanced-subcollection consequence of a separate colorful hypothesis.

The stronger four-block application is an open direction, not an established result. The paper does not claim a new fastest general-IP algorithm, a practical solver speedup, or established novelty over all later literature.

## Verification and review status

- The source compiled successfully with the Codex built-in LaTeX compiler.
- The PDF was also built locally with pdfLaTeX, with resolved cross-references.
- The final build was checked for undefined references and overfull boxes, and rendered pages were inspected.
- No computational experiments or formal proof verification are claimed.

The first substantive review priorities are:

1. Independently assess the geometric hypothesis and pin a source revision before any external submission.
2. Audit novelty of the Euclidean-column Graver bound against determinant-, circuit-, and discrepancy-based results.
3. Compare the bounded-variable proximity theorem against the applicable extensions of later proximity results.
4. Substitute the two-level bound into a specific block-aware augmentation algorithm and account for initialization, step lengths, and iteration complexity.
5. Complete the separate four-block/colorful argument without assuming that derived vectors retain the sparsity of the original columns.

## Building

Open `main.tex` in the Codex built-in LaTeX editor for an editable source and live PDF preview. With a local TeX installation, run the following twice from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The tracked PDF is a reading copy; regenerate it after changing the source.
