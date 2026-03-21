---
permalink: /
title: ""
author_profile: true
description: "Oscar Mañas — Research Scientist at Meta Superintelligence Labs working on multimodal generative AI, vision-language models, and text-to-image/video generation."
redirect_from:
  - /about/
  - /about.html
---

Hola! I'm Oscar Mañas. I'm a **Research Scientist at [Meta Superintelligence Labs](https://ai.meta.com/)** on the GenMedia team in Zurich. I recently completed my PhD at [Mila](https://mila.quebec/en/) and [Université de Montréal](https://diro.umontreal.ca/english/home/), advised by Prof. [Aishwarya Agrawal](https://www.iro.umontreal.ca/~agrawal/).

My research explores the intersection of vision and language, with a focus on **multimodal vision-language generative models**: systems capable of generating images, videos and text from multimodal inputs. I'm especially interested in building models that reason fluidly across modalities, treating them as complementary channels of perception and thought.

Previously, I was a Visiting Researcher at [Meta FAIR](https://ai.meta.com/research/) and a Research Intern at [Element AI](https://www.elementai.com/research). See my [CV](/cv/) for more details.

## News

<div class="news-list" markdown="0">
<table>
<tr><td>Feb 2026</td><td>PhD thesis published: <a href="https://hdl.handle.net/1866/44263"><em>Towards efficient, reliable and measurable vision-language systems</em></a></td></tr>
<tr><td>Nov 2025</td><td>Defended my <strong>PhD thesis</strong> and graduated from Mila / Université de Montréal</td></tr>
<tr><td>Oct 2025</td><td>Started as <strong>Research Scientist</strong> at <a href="https://ai.meta.com/">Meta Superintelligence Labs</a>, GenMedia team, Zurich</td></tr>
<tr><td>2025</td><td>Paper accepted at <strong>ICCV 2025</strong>: <a href="https://arxiv.org/abs/2508.11616">Controlling Multimodal LLMs via Reward-guided Decoding</a></td></tr>
<tr><td>2024</td><td>Paper accepted at <strong>TMLR</strong>: <a href="https://arxiv.org/abs/2403.17804">Improving Text-to-Image Consistency via Automatic Prompt Optimization</a></td></tr>
<tr><td>2024</td><td>Paper accepted at <strong>AAAI 2024</strong>: <a href="https://arxiv.org/abs/2310.02567">Improving Automatic VQA Evaluation Using Large Language Models</a></td></tr>
</table>
</div>

## Selected Publications

{% assign selected = site.publications | where: "selected", true | sort: "year" | reverse %}
{% for post in selected %}
  {% include archive-single.html %}
{% endfor %}

<a href="/publications/" class="btn btn--inverse">View all publications &rarr;</a>
