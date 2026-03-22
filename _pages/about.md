---
permalink: /
title: ""
author_profile: true
description: "Oscar Mañas — Research Scientist at Meta Superintelligence Labs working on multimodal generative AI, vision-language models, and text-to-image/video generation."
redirect_from:
  - /about/
  - /about.html
---

Hola! I'm Oscar Mañas. I'm a **Research Scientist at [Meta Superintelligence Labs](https://ai.meta.com/)** on the Media Generation team in Zurich. I recently completed my PhD at [Mila](https://mila.quebec/en/) and [Université de Montréal](https://diro.umontreal.ca/english/home/), advised by Prof. [Aishwarya Agrawal](https://www.iro.umontreal.ca/~agrawal/).

My research explores the intersection of vision and language, with a focus on **multimodal vision-language generative models**: systems capable of generating images, videos and text from multimodal inputs. I'm especially interested in building models that reason fluidly across modalities, treating them as complementary channels of perception and thought.

Previously, I was a Visiting Researcher at [Meta FAIR](https://ai.meta.com/research/) and a Research Intern at [Element AI](https://www.elementai.com/research). See my [CV](/cv/) for more details.

## News

<div class="news-list" markdown="0">
<ul>
<li><span class="news-date">Feb 2026</span> PhD thesis published: <a href="https://hdl.handle.net/1866/44263"><em>Towards efficient, reliable and measurable vision-language systems</em></a></li>
<li><span class="news-date">Dec 2025</span> Spotlight talk at the <a href="https://sites.google.com/view/dlbcn2025/program/talks">Deep Learning Barcelona Symposium</a> (<a href="https://www.youtube.com/live/Xz7Est3JlBw?si=ZIT4hey-Zy6vm30n&t=9521">recording</a>)</li>
<li><span class="news-date">Nov 2025</span> Defended my PhD thesis and graduated from Mila / Université de Montréal</li>
<li><span class="news-date">Oct 2025</span> Started as Research Scientist at <a href="https://ai.meta.com/">Meta Superintelligence Labs</a>, Media Generation team, Zurich</li>
<li><span class="news-date">Jun 2025</span> Paper accepted at <a href="https://arxiv.org/abs/2508.11616">ICCV 2025</a>: <em>Controlling Multimodal LLMs via Reward-guided Decoding</em></li>
<li><span class="news-date">Jun 2024</span> Paper accepted at <a href="https://arxiv.org/abs/2403.17804">TMLR</a>: <em>Improving Text-to-Image Consistency via Automatic Prompt Optimization</em></li>
<li><span class="news-date">Jan 2024</span> Started as Visiting Researcher at <a href="https://ai.meta.com/research/">Meta FAIR</a>, Montreal</li>
<li><span class="news-date">Dec 2023</span> Paper accepted at <a href="https://arxiv.org/abs/2310.02567">AAAI 2024</a>: <em>Improving Automatic VQA Evaluation Using Large Language Models</em></li>
<li><span class="news-date">Jun 2023</span> Started as Research Scientist Intern at <a href="https://ai.meta.com/research/">Meta FAIR</a>, Montreal</li>
</ul>
</div>

## Selected Publications

{% assign selected = site.publications | where: "selected", true | sort: "sort_date" | reverse %}
{% for post in selected %}
  {% include archive-single.html %}
{% endfor %}

<a href="/publications/" class="btn btn--inverse">View all publications &rarr;</a>
