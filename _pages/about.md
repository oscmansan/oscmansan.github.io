---
permalink: /
title: ""
author_profile: true
description: "Oscar Mañas — Research Scientist at Meta working on multimodal AI: vision-language models, and image, video and text generation."
redirect_from:
  - /about/
  - /about.html
---

Hola! I'm Oscar Mañas. I'm a **Research Scientist at [Meta](https://ai.meta.com/)** in Zurich, working on multimodal AI. I recently completed my PhD at [Mila](https://mila.quebec/en/) and [Université de Montréal](https://diro.umontreal.ca/english/home/), advised by Prof. [Aishwarya Agrawal](https://www.iro.umontreal.ca/~agrawal/).

My research explores the intersection of vision and language, with a focus on **multimodal generative models**: systems capable of generating images, videos, text and actions from multimodal inputs. I'm especially interested in building models that reason fluidly across modalities, treating them as **complementary channels of perception, thought and interaction**. In practice, a through-line in my work is the loop between **generation, understanding, and evaluation**: building reward models and metrics, and using them to steer model behavior.

Previously, I was a Visiting Researcher at [Meta FAIR](https://ai.meta.com/research/) and a Research Intern at [Element AI](https://www.elementai.com/research). My work has been published at CVPR, ICML, ICCV, AAAI, EACL, and TMLR. See my [CV](/cv/) for more details.

## Selected Publications

{% assign selected = site.publications | where: "selected", true | sort: "sort_date" | reverse %}
{% for post in selected %}
  {% include archive-single.html %}
{% endfor %}

<a href="/publications/" class="btn btn--inverse">View all publications &rarr;</a>

## News

<div class="news-list" markdown="0">
<ul>
<li><time class="news-date" datetime="2026-05">May 2026</time> Paper accepted at <strong>ICML 2026</strong>: <em><a href="https://arxiv.org/abs/2602.00462">LatentLens: Revealing Highly Interpretable Visual Tokens in LLMs</a></em></li>
<li><time class="news-date" datetime="2026-02">Feb 2026</time> Paper accepted at <strong>CVPR 2026</strong>: <em><a href="https://arxiv.org/abs/2506.01085">Learning What Matters: Prioritized Concept Learning via Relative Error-driven Sample Selection</a></em></li>
<li><time class="news-date" datetime="2026-02">Feb 2026</time> PhD thesis published: <em><a href="https://hdl.handle.net/1866/44263">Towards efficient, reliable and measurable vision-language systems</a></em></li>
<li><time class="news-date" datetime="2025-12">Dec 2025</time> Preprint released: <em><a href="https://arxiv.org/abs/2512.13019">SneakPeek: Future-Guided Instructional Streaming Video Generation</a></em></li>
<li><time class="news-date" datetime="2025-12">Dec 2025</time> Spotlight talk at the <a href="https://sites.google.com/view/dlbcn2025/program/talks">Deep Learning Barcelona Symposium</a> (<a href="https://www.youtube.com/live/Xz7Est3JlBw?si=ZIT4hey-Zy6vm30n&amp;t=9521">recording</a>)</li>
<li><time class="news-date" datetime="2025-11">Nov 2025</time> Defended my PhD thesis and graduated from Mila / Université de Montréal</li>
</ul>
</div>

<a href="/news/">All news &rarr;</a>
