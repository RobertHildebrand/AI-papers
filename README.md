# AI-generated papers

This repository collects AI-generated and AI-assisted papers that I create. It is a home for exploratory research, mathematical notes, revised arguments, and other paper-length projects developed with AI.

These papers are not necessarily intended for publication in a journal. Some are working drafts, personal investigations, or exercises in developing and documenting ideas. Their presence here does not imply that they have been peer reviewed or prepared for formal publication.

## Contributions

I welcome improvements to the work in this repository through pull requests, including corrections, clearer proofs, extensions, and formal verifications in Lean. Contributions that identify gaps or verify mathematical claims are especially welcome.

## Papers

- [Extension Complexity Lower Bounds for Mixed-Integer Extended Formulations: A corrected argument using families of formulations](matching-milef-revision/main-online-revised.tex). An AI-assisted revision of an earlier paper by Robert Hildebrand, Robert Weismantel, and Rico Zenklusen. The draft gives a weaker lower bound using a family of formulations, explains the error in the original proof, and discusses the stronger results of Cevallos, Weltge, and Zenklusen. The LaTeX source is self-contained, including its bibliography.

- [Euclidean Steinitz Bounds for Graver Bases and Integer Programming](euclidean-steinitz-ip/main.tex) ([PDF](euclidean-steinitz-ip/main.pdf)). An AI-generated working draft deriving Graver, proximity, finite-state, and two-level block-matrix bounds from an explicit Euclidean Steinitz hypothesis. Includes literature comparisons and separates proved conditional consequences from the open four-block application.

## Versions and citations

To cite an individual preprint, use the BibTeX entry in its directory. Each paper provides a copyable citation in its README and a downloadable `citation.bib` file:

- [Euclidean Steinitz bounds](euclidean-steinitz-ip/README.md#citation) ([BibTeX](euclidean-steinitz-ip/citation.bib)).
- [Corrected matching MILEF argument](matching-milef-revision/README.md#citation) ([BibTeX](matching-milef-revision/citation.bib)).

These entries identify the dated working drafts. When citing a particular argument or theorem, also identify the exact revision: replace `main` in the citation URL with the full Git commit identifier of the version you read, and record that identifier in the `note` field. A commit permalink fixes the version; a `main` link follows later edits. Only use a commit that contains the cited manuscript.

Preserve released revisions in Git history and record substantive corrections as new commits. The draft date is not a DOI, release tag, or claim of peer review.

The suggested entries are title-led. Repository ownership, curation, and use of an AI tool do not by themselves establish manuscript authorship. If a confirmed author list is adopted for a revision, update its citation accordingly. For AI-assisted revisions of earlier work, cite the original work separately when discussing its results and identify this repository version when discussing its changes; retaining original names in a source file does not establish approval of the AI-assisted revision.
