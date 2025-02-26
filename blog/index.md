---
layout: default
title: "Blogginlägg"
permalink: /blog/
---

<h1>Blogginlägg</h1>
<ul>
  {% for post in site.blog | sort: 'date' | reverse %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%Y-%m-%d" }}
    </li>
  {% endfor %}
</ul>
