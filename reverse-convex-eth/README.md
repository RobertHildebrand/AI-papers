# An ETH Lower Bound for Reverse-Convex Integer Feasibility with a Boundary Hyperplane Cover

Research question and direction: **Robert Hildebrand**. AI-assisted mathematical draft, October 26, 2026. Not peer reviewed; no claim of literature priority.

- [Manuscript (PDF)](main.pdf)
- [Self-contained LaTeX source](main.tex)
- [BibTeX citation](citation.bib)
- [Exhaustive small-instance checker](verify_reduction.py)

The note reduces k-Clique to integer feasibility in a box minus the interiors of axis-aligned rational boxes. The dimension is n=k, the supplied boundary cover has d=2k(N+1) hyperplanes, and the instance has polynomial encoding length L. Assuming ETH, no deterministic algorithm has running time f(n)d^{o(n)}L^{O(1)}. The problem is also W[1]-hard parameterized by dimension.

The excluded-set count grows with the graph. The result does not settle fixed total m, rule out moving the exponent into L, prove an exact d^n lower bound, or require explicit arrangement enumeration.

## Build and verify

Run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice to build the PDF. The bibliography is included in the source. Run `python3 verify_reduction.py` to exhaustively check all simple graphs on two through four vertices and every target size from two through the graph order.

## Contributions

Robert Hildebrand formulated the research question and directed the investigation. OpenAI Codex assisted with developing the reduction, drafting the mathematical argument and exposition, and implementing and running the finite verification checks. This credits Hildebrand's research contribution without asserting completed review or approval of every mathematical claim.

## Citation

*An ETH Lower Bound for Reverse-Convex Integer Feasibility with a Boundary Hyperplane Cover*. AI-papers repository working draft, October 26, 2026. Research question and direction by Robert Hildebrand; mathematical development and drafting assisted by OpenAI Codex.

```bibtex
@misc{AIpapers:ReverseConvexETH:2026,
  key          = {ETH Lower Bound for Reverse-Convex Integer Feasibility},
  title        = {{An ETH Lower Bound for Reverse-Convex Integer Feasibility with a Boundary Hyperplane Cover}},
  howpublished = {AI-papers repository preprint},
  year         = {2026},
  month        = oct,
  url          = {https://github.com/RobertHildebrand/AI-papers/tree/main/reverse-convex-eth},
  note         = {Research question and direction by Robert Hildebrand; AI-assisted working draft dated October 26, 2026}
}
```

For a particular theorem or argument, replace `main` in the URL with the full Git commit identifier containing the cited manuscript, and record that identifier in the `note` field. The title-led citation follows this repository's convention; repository ownership and AI assistance do not themselves establish authorship. Update the citation if a confirmed author list is adopted.

The manuscript separately cites Hildebrand and Göß (arXiv:2409.05308v2) for the boundary-cover framework and Chen, Huang, Kanj, and Xia (JCSS, 2006) for the parameterized Clique lower bound.
