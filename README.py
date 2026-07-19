from pathlib import Path
import pypandoc

content = r'''# (Use this content as README.md)

<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=1000&color=FF6B6B,F7B32B,4ECDC4,556270&center=true&vCenter=true&width=700&lines=Hi+there,+I'm+Rishabh+👋;Java+Full+Stack+Developer;Spring+Boot+%7C+React+%7C+DSA;Always+Learning+🚀"/>
</h1>

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=header"/>
</p>

## 🚀 About Me

- 🎓 B.Tech CSE Student
- 💻 Java Full Stack Developer
- 🧠 500+ DSA Problems Solved
- 🌱 Learning Spring Boot, React & System Design
- 🚀 Looking for SDE / Java Backend opportunities

<p>
<img src="https://skillicons.dev/icons?i=java,spring,react,js,html,css,mysql,postgres,git,github&theme=dark"/>
</p>

---

## 📊 GitHub Stats

<p align="center">
<img height="170" src="https://github-readme-stats.vercel.app/api?username=rishabhdav&show_icons=true&theme=radical&hide_border=true"/>
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=rishabhdav&layout=compact&theme=radical&hide_border=true"/>
</p>

<p align="center">
<img src="https://github-readme-streak-stats.herokuapp.com/?user=rishabhdav&theme=radical&hide_border=true"/>
</p>

<p align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=rishabhdav&theme=radical&hide_border=true"/>
</p>

---

## 🏆 Coding Platforms

<table align="center">
<tr>
<td><a href="https://leetcode.com/u/rishabhtri/"><img src="https://leetcard.jacoblin.cool/rishabhtri?theme=dark"/></a></td>
<td><a href="https://www.geeksforgeeks.org/profile/rishabhtricywd"><img src="https://gfgstatscard.vercel.app/rishabhtricywd"/></a></td>
</tr>
<tr>
<td><a href="https://codolio.com/profile/mHlpjSWV"><img src="https://img.shields.io/badge/Codolio-View_Profile-6C5CE7?style=for-the-badge"/></a></td>
<td><a href="https://www.codechef.com/users/bright_card_63"><img src="https://cp-logo.vercel.app/codechef/bright_card_63"/></a></td>
</tr>
</table>

<p align="center">
<img src="https://leetcard.jacoblin.cool/rishabhtri?theme=dark&ext=heatmap"/>
</p>

---

## 🚀 Featured Projects

<p align="center">
<a href="https://github.com/rishabhdav/ecommerce"><img src="https://github-readme-stats.vercel.app/api/pin/?username=rishabhdav&repo=ecommerce&theme=radical&hide_border=true"/></a>
<a href="https://github.com/rishabhdav/BlogApplicationApi"><img src="https://github-readme-stats.vercel.app/api/pin/?username=rishabhdav&repo=BlogApplicationApi&theme=radical&hide_border=true"/></a>
</p>

<p align="center">
<a href="https://github.com/rishabhdav/DataWarehouseAnalytics"><img src="https://github-readme-stats.vercel.app/api/pin/?username=rishabhdav&repo=DataWarehouseAnalytics&theme=radical&hide_border=true"/></a>
</p>

---

## 🌐 Connect With Me

<p align="center">
<a href="https://www.linkedin.com/in/rishabh-tripathi-096833284/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin"/></a>
<a href="https://leetcode.com/u/rishabhtri/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode"/></a>
<a href="https://www.geeksforgeeks.org/profile/rishabhtricywd"><img src="https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge&logo=geeksforgeeks"/></a>
<a href="https://codolio.com/profile/mHlpjSWV"><img src="https://img.shields.io/badge/Codolio-6C5CE7?style=for-the-badge"/></a>
<a href="https://www.codechef.com/users/bright_card_63"><img src="https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge"/></a>
</p>

<p align="center">
<img src="https://github-profile-trophy.vercel.app/?username=rishabhdav&theme=radical&no-frame=true&row=1&column=6"/>
</p>

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer"/>
</p>
'''
Path('/mnt/data/README.md').write_text(content,encoding='utf-8')
print('done')
