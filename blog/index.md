---
layout: default
title: "KPLN-blogg"
permalink: /blog/
---

<h1>KPLN-blogg</h1>
<p>Använd menyn för att välja ämnen att läsa om.</p>
<ul>
  {% for post in site.blog | sort: 'date' | reverse %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%Y-%m-%d" }}
    </li>
  {% endfor %}
</ul>
