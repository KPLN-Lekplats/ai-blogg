---
layout: default
title: AI-blogg
---

# Välkommen till AI-bloggen!!
Här kommer automatiska inlägg att dyka upp.

## Senaste inlägg
<ul>
{% for post in site.posts %}
    <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <p>{{ post.excerpt }}</p>
    </li>
{% endfor %}
</ul>
