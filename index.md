---
layout: default
title: "Välkommen till KPLN-bloggen!"
---

<!-- Navigationsmeny -->
<nav>
  <ul>
    <li><a href="{{ site.baseurl }}/">Hem</a></li>
    <li><a href="{{ site.baseurl }}/blog/">Blogginlägg</a></li>
    <li><a href="https://www.kpln.se">KPLN.se</a></li>
  </ul>
</nav>

<h1>Välkommen till bloggen!</h1>
<p>Bloggen om lekplats, sport och träning för utomhusmiljöer.</p>

<h2>Senaste inlägg</h2>
<ul>
  {% for post in site.blog | sort: 'date' | reverse %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%Y-%m-%d" }}
    </li>
  {% endfor %}
</ul>
