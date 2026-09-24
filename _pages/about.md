---
permalink: /
title: ""
seo_title: "Oscar Mañas — Research Scientist, Multimodal AI"
author_profile: true
description: "Oscar Mañas (Oscar Manas) — Research Scientist at Meta Superintelligence Labs. Multimodal AI: vision-language models, world models, and embodied and physical AI (VLAs, WAMs)."
redirect_from:
  - /about/
  - /about.html
---

<div class="bio" markdown="1">

Hola! I'm Oscar Mañas, a **Research Scientist at [Meta Superintelligence Labs](https://ai.meta.com/)** in Zurich, working on multimodal AI. I recently completed my PhD at [Mila](https://mila.quebec/en/) and [Université de Montréal](https://diro.umontreal.ca/english/home/), advised by Prof. [Aishwarya Agrawal](https://www.iro.umontreal.ca/~agrawal/).

Images, video, language, and even actions are different aspects of the same underlying reality. I build **multimodal models** that understand and generate images, video, and text, along with the metrics and reward models that evaluate and steer them. Lately, I've been drawn to **embodied and physical AI**. I believe that vision-language-action models (VLAs) and world-action models (WAMs) are the natural next step for VLMs and video world models: actions are just another modality represented as a sequence of embeddings. What a model learns from observation can then carry over to action, and from there, to improving itself through its own experience.

Previously, I was a Visiting Researcher at [Meta FAIR](https://ai.meta.com/research/) and a Research Intern at [Element AI](https://www.elementai.com/research). My work has been published at CVPR, ICML, ICCV, AAAI, EACL, and TMLR. See my [CV](/cv/) for more details.

</div>

## News

<div class="news-list" markdown="0">
<ul>
<li><span class="news-date">May 2026</span> Paper accepted at <strong>ICML 2026</strong>: <em><a href="https://arxiv.org/abs/2602.00462">LatentLens: Revealing Highly Interpretable Visual Tokens in LLMs</a></em></li>
<li><span class="news-date">Feb 2026</span> Paper accepted at <strong>CVPR 2026</strong>: <em><a href="https://arxiv.org/abs/2506.01085">Learning What Matters: Prioritized Concept Learning via Relative Error-driven Sample Selection</a></em></li>
<li><span class="news-date">Feb 2026</span> PhD thesis published: <em><a href="https://hdl.handle.net/1866/44263">Towards efficient, reliable and measurable vision-language systems</a></em></li>
<li><span class="news-date">Dec 2025</span> Preprint released: <em><a href="https://arxiv.org/abs/2512.13019">SneakPeek: Future-Guided Instructional Streaming Video Generation</a></em></li>
<li><span class="news-date">Dec 2025</span> Spotlight talk at the <a href="https://sites.google.com/view/dlbcn2025/program/talks">Deep Learning Barcelona Symposium</a> (<a href="https://www.youtube.com/live/Xz7Est3JlBw?si=ZIT4hey-Zy6vm30n&t=9521">recording</a>)</li>
</ul>
<details>
<summary>Show older news</summary>
<ul>
<li><span class="news-date">Nov 2025</span> Defended my PhD thesis and graduated from Mila / Université de Montréal</li>
<li><span class="news-date">Oct 2025</span> Started as Research Scientist at <a href="https://ai.meta.com/">Meta Superintelligence Labs</a>, Zurich</li>
<li><span class="news-date">Jun 2025</span> Paper accepted at <strong>ICCV 2025</strong>: <em><a href="https://arxiv.org/abs/2508.11616">Controlling Multimodal LLMs via Reward-guided Decoding</a></em></li>
<li><span class="news-date">Jun 2024</span> Paper accepted at <strong>TMLR</strong>: <em><a href="https://arxiv.org/abs/2403.17804">Improving Text-to-Image Consistency via Automatic Prompt Optimization</a></em></li>
<li><span class="news-date">Jan 2024</span> Started as Visiting Researcher at <a href="https://ai.meta.com/research/">Meta FAIR</a>, Montreal</li>
<li><span class="news-date">Dec 2023</span> Paper accepted at <strong>AAAI 2024</strong>: <em><a href="https://arxiv.org/abs/2310.02567">Improving Automatic VQA Evaluation Using Large Language Models</a></em></li>
<li><span class="news-date">Jun 2023</span> Started as Research Scientist Intern at <a href="https://ai.meta.com/research/">Meta FAIR</a>, Montreal</li>
</ul>
</details>
</div>

## Selected Publications

{% assign selected = site.publications | where: "selected", true | sort: "sort_date" | reverse %}
{% for post in selected %}
  {% include archive-single.html %}
{% endfor %}

<a href="/publications/" class="more-link">All publications &rarr;</a>
