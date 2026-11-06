# Generates all pages from shared components (header/footer). Run: python3 build.py
import os
NAV=[("index.html","Home"),("ai-tools.html","AI Tools"),("productivity-tools.html","Productivity"),("tutorials.html","Tutorials"),("about.html","About"),("contact.html","Contact")]
def page(fn,title,desc,body,hero=False):
    links="".join(f'<li><a href="{h}"{" class=on aria-current=page" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#0b0e17"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/css/style.css"></head><body>
<header><div class="wrap nav"><a class="logo" href="index.html">Tharun <span>Tech Hub</span></a><button id="mb" aria-label="Menu" aria-expanded="false">Menu</button><ul class="links" id="nav">{links}</ul></div></header>
<main>{body}</main>
<footer><div class="wrap fg"><div><a class="logo" href="index.html">Tharun <span>Tech Hub</span></a><p>Independent guides to AI tools and productivity software.</p></div>
<ul><li><a href="privacy-policy.html">Privacy Policy</a></li><li><a href="affiliate-disclosure.html">Affiliate Disclosure</a></li><li><a href="contact.html">Contact</a></li></ul>
<p style="width:100%">&copy; <span id="y">2026</span> Tharun Tech Hub. Some links on this site may be affiliate links. Product names belong to their respective owners; no partnership or endorsement is implied.</p></div></footer>
<script src="assets/js/main.js"></script></body></html>'''
def cards(items):
    return '<div class="grid">'+"".join(f'<article class="card"><span class="tag">{t}</span><h3>{h}</h3><p>{p}</p>{x}</article>' for t,h,p,x in items)+'</div>'
def ul(*a): return "<ul>"+"".join(f"<li>{i}</li>" for i in a)+"</ul>"
DISC='<div class="note"><strong>Disclosure:</strong> Some links on this page may be affiliate links. If you sign up through them we may earn a commission at no extra cost to you. See our <a href="affiliate-disclosure.html">Affiliate Disclosure</a>. We are not an official partner of any tool listed unless stated.</div>'
P={}
P["index.html"]=("Tharun Tech Hub | AI Tools, Productivity Software & Tutorials","Discover AI tools, productivity software and beginner-friendly tech tutorials for students, creators, freelancers and professionals.",
f'''<section class="hero"><div class="wrap hero-in"><h1>Discover Smarter Ways to Work with <span class="g">Technology.</span></h1>
<p>Explore AI tools, productivity resources and digital solutions, explained in plain language for students, creators, freelancers and professionals.</p>
<a class="btn p" href="ai-tools.html">Explore Tools</a> <a class="btn" href="tutorials.html">Read Tutorials</a></div></section>
<section><div class="wrap"><h2>Featured resources</h2><p>Start with one of these guides and sections.</p>'''+cards([
("AI Tools","Which AI assistant fits your work?","Compare ChatGPT, Claude, Gemini and Perplexity by use case.",'<a href="ai-tools.html">Browse AI tools</a>'),
("Productivity","Understand link management with Dub","What short links are and how click analytics help you learn what works.",'<a href="productivity-tools.html">See productivity tools</a>'),
("Tutorial","Write better AI prompts","A simple four-part structure that gets clearer answers.",'<a href="tutorials.html#prompts">Read the guide</a>'),
("Tutorial","Track your links the right way","Use UTM tags and short links to measure where visitors come from.",'<a href="tutorials.html#links">Read the guide</a>')])+DISC+'</div></section>')
P["ai-tools.html"]=("AI Tools Guide | Tharun Tech Hub","Plain-language overview of popular AI tools like ChatGPT, Claude, Gemini and Perplexity: features, benefits and use cases.",
'<section class="page"><div class="wrap"><h1>AI tools, explained</h1><p>Short overviews of widely used AI tools. Features and pricing change often, so always check each official website for current details. Tharun Tech Hub is not affiliated with or endorsed by any company listed here.</p>'+cards([
("Assistant","ChatGPT (OpenAI)","A general-purpose AI chat assistant for writing, brainstorming, coding help and analysis.",ul("Best for: drafting, summarising, learning topics","Use case: turn rough notes into a clear email")),
("Assistant","Claude (Anthropic)","An AI assistant known for working with long documents and careful writing.",ul("Best for: reading reports, editing, coding help","Use case: summarise a long PDF and list action items")),
("Assistant","Google Gemini","Google's AI assistant, connected to Google's ecosystem of products.",ul("Best for: people already using Google apps","Use case: brainstorm ideas, then organise them")),
("Research","Perplexity","An AI-powered search tool that answers questions with source links.",ul("Best for: quick research with citations","Use case: find sources for a student assignment")),
("Design","Canva (Magic tools)","Design platform with built-in AI features for graphics and presentations.",ul("Best for: creators and small businesses","Use case: social posts and simple slide decks")),
("Notes","Notion AI","AI features inside the Notion workspace for notes and documents.",ul("Best for: organised notes and team docs","Use case: clean up meeting notes"))])+'<div class="note">Tip: AI can make mistakes. Verify important facts, and never paste private or confidential information into any AI tool.</div></div></section>')
P["productivity-tools.html"]=("Productivity Tools & Link Management | Tharun Tech Hub","Learn about link management, analytics and automation tools, including an educational introduction to Dub for shortening links and tracking performance.",
'<section class="page"><div class="wrap"><h1>Productivity tools</h1><p>Software that saves time, keeps work organised and shows what is working.</p>'+DISC+
'<h2 style="margin-top:40px">What is Dub?</h2><div class="card"><span class="tag">Link management</span><h3>Dub (dub.co)</h3><p>Dub is a link management platform. It lets you turn long URLs into short, branded links and see how those links perform.</p>'+ul("Shorten links: create short, shareable URLs","Understand performance: view clicks and where traffic comes from","Organise: keep many links in one dashboard","Use case: share one link on WhatsApp or social media and see which channel gets clicks")+'<p><a href="https://dub.co" rel="noopener" target="_blank">Visit dub.co</a> (official site, not an affiliate link). Tharun Tech Hub is not an official Dub partner.</p></div>'
'<h2 style="margin-top:40px">Other helpful tools</h2>'+cards([
("Automation","Zapier","Connects apps so tasks happen automatically, such as saving form replies to a spreadsheet.",""),
("Workspace","Notion","Notes, tasks and wikis in one place for personal or team use.",""),
("Analytics","Google Analytics","Free website analytics that show visits, pages and traffic sources.","")])+'</div></section>')
P["tutorials.html"]=("Beginner Tutorials | Tharun Tech Hub","Beginner-friendly guides on using AI tools, improving productivity and managing and tracking links.",
'<section class="page"><div class="wrap prose" style="max-width:820px"><h1>Beginner tutorials</h1><p>Short, practical guides. Tap a title to open it.</p>'
'<details id="start" open><summary>How to start using an AI tool</summary><ol><li>Pick one tool and create a free account.</li><li>Start with a small task, like rewriting an email.</li><li>Review the answer and ask follow-up questions.</li><li>Check facts before you rely on them.</li></ol></details>'
'<details id="prompts"><summary>How to write better AI prompts</summary><ol><li>Say who you are or the role you want it to play.</li><li>State the task clearly.</li><li>Add context: audience, length, tone.</li><li>Ask for a format, such as a table or bullet list.</li></ol></details>'
'<details id="focus"><summary>How to improve your productivity</summary><ul><li>Write your top three tasks each morning.</li><li>Work in 25-minute focus blocks with short breaks.</li><li>Batch similar tasks, like replying to messages.</li><li>Automate repeat work when a tool can do it.</li></ul></details>'
'<details id="links"><summary>How to manage and track links</summary><ol><li>Create a short link for each place you share, such as WhatsApp Status or a social post.</li><li>Add UTM tags (source, medium, campaign) so analytics show where visitors came from.</li><li>Use a link tool such as <a href="productivity-tools.html">Dub</a> to view clicks.</li><li>Compare results and keep what works.</li></ol></details>'
+DISC+'</div></section>')
P["about.html"]=("About Tharun Siddha | Tharun Tech Hub","Meet Tharun Siddha, founder of Tharun Tech Hub, and learn our mission to make technology easier to understand and use.",
'<section class="page"><div class="wrap prose"><h1>About Tharun Tech Hub</h1><p>Tharun Tech Hub is an independent website about AI tools, productivity software and digital resources.</p>'
'<h2>Founder</h2><p>Tharun Siddha started Tharun Tech Hub to share what he learns about useful technology. <!-- Add your own short bio here: background, studies, interests. --></p>'
'<h2>Our mission</h2><p>Make technology easier to understand and use, so students, creators, freelancers and professionals can save time and do better work.</p>'
'<h2>How we work</h2>'+ul("Plain-language explanations with no hype","Clear disclosure of any affiliate links","No invented reviews, statistics or partnerships")+'<p style="margin-top:20px"><a class="btn p" href="contact.html">Get in touch</a></p></div></section>')
P["contact.html"]=("Contact | Tharun Tech Hub","Contact Tharun Tech Hub with questions, feedback or collaboration enquiries.",
'<section class="page"><div class="wrap"><h1>Contact</h1><p>Questions, feedback or ideas for a tutorial? Send a message.</p>'
'<form id="cf" data-endpoint="YOUR_FORM_ENDPOINT_URL"><div><label for="n">Name</label><input id="n" name="name" required></div><div><label for="e">Email</label><input id="e" name="email" type="email" required></div>'
'<div><label for="t">Topic</label><select id="t" name="topic"><option>General question</option><option>Feedback</option><option>Collaboration</option></select></div><div><label for="m">Message</label><textarea id="m" name="message" rows="5" required></textarea></div>'
'<button class="btn p" type="submit">Send message</button><p id="st" role="status"></p></form>'
'<div class="grid"><div class="card"><h3>Email</h3><p>[your-email@example.com]</p></div><div class="card"><h3>WhatsApp Channel</h3><p>[add your channel link]</p></div><div class="card"><h3>Social media</h3><p>[add your profile links]</p></div></div></div></section>')
P["privacy-policy.html"]=("Privacy Policy | Tharun Tech Hub","How Tharun Tech Hub collects, uses and protects information.",
'<section class="page"><div class="wrap prose"><h1>Privacy Policy</h1><p>Last updated: [add date]</p><h2>Information we collect</h2><p>If you use the contact form, we receive the name, email and message you submit. We use it only to reply to you.</p>'
'<h2>Analytics and cookies</h2><p>This site may use analytics or cookies in future to understand visits. If we add them, this policy will be updated.</p><h2>Third-party links</h2><p>We link to other websites, including tools with affiliate links. Their privacy practices are their own.</p>'
'<h2>Your choices</h2><p>You can ask us to delete any information you sent by contacting us through the <a href="contact.html">contact page</a>.</p><p>This page is a general template and not legal advice. Review it for your needs.</p></div></section>')
P["affiliate-disclosure.html"]=("Affiliate Disclosure | Tharun Tech Hub","Tharun Tech Hub may earn commissions from affiliate links. Read how we disclose and handle them.",
'<section class="page"><div class="wrap prose"><h1>Affiliate Disclosure</h1><p>Some links on Tharun Tech Hub may be affiliate links. If you click one and sign up or buy, we may earn a commission at no extra cost to you.</p>'
'<h2>Our approach</h2>'+ul("We mark pages that contain affiliate links.","Affiliate links use rel=\"sponsored\".","Commissions do not change the price you pay.","We describe tools honestly and aim to be accurate.")+
'<h2>No implied partnerships</h2><p>Mentioning a product does not mean it endorses us or that we are an official partner. We will state clearly if that ever changes.</p></div></section>')
for fn,(t,d,b) in P.items(): open(fn,"w").write(page(fn,t,d,b))
