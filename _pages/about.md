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
<ul>
<li><span class="news-date">Feb 2026</span> PhD thesis published: <a href="https://hdl.handle.net/1866/44263"><em>Towards efficient, reliable and measurable vision-language systems</em></a></li>
<li><span class="news-date">Nov 2025</span> Defended my <strong>PhD thesis</strong> and graduated from Mila / Université de Montréal</li>
<li><span class="news-date">Oct 2025</span> Started as <strong>Research Scientist</strong> at <a href="https://ai.meta.com/">Meta Superintelligence Labs</a>, GenMedia team, Zurich</li>
<li><span class="news-date">2025</span> Paper accepted at <strong>ICCV 2025</strong>: <a href="https://arxiv.org/abs/2508.11616">Controlling Multimodal LLMs via Reward-guided Decoding</a></li>
<li><span class="news-date">2024</span> Paper accepted at <strong>TMLR</strong>: <a href="https://arxiv.org/abs/2403.17804">Improving Text-to-Image Consistency via Automatic Prompt Optimization</a></li>
<li><span class="news-date">2024</span> Paper accepted at <strong>AAAI 2024</strong>: <a href="https://arxiv.org/abs/2310.02567">Improving Automatic VQA Evaluation Using Large Language Models</a></li>
</ul>
</div>

## Selected Publications

{% assign selected = site.publications | where: "selected", true | sort: "year" | reverse %}
{% for post in selected %}
  {% include archive-single.html %}
{% endfor %}

<a href="/publications/" class="btn btn--inverse">View all publications &rarr;</a>
