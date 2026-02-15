# 🛠 Microbex Website — Development Workflow

This document explains the basic workflow for building and updating the Microbex website using **GitHub**, **GitHub Desktop**, **VS Code**, and **Cloudflare Pages**.

---

## 1. Branch Structure

### **main**
- Live production branch  
- Automatically deployed to **https://microbex.in**

### **development**
- All new work happens here  
- Test and verify changes before merging to `main`

---

## 2. Local Development (VS Code)

1. Open **GitHub Desktop**
2. Switch to the **development** branch
3. Click **“Open in VS Code”**
4. Make your changes (HTML, CSS, JS)
5. Test locally by opening the HTML file in your browser

---

## 3. Commit & Push (GitHub Desktop)

After making changes:

1. Go to GitHub Desktop  
2. Review changed files  
3. Add a short commit message  
4. Click **“Commit to development”**  
5. Click **“Push origin”**

This sends your code to the GitHub `development` branch.

---

## 4. Deploying to Production (Cloudflare Pages)

Cloudflare deploys automatically from the **main** branch.

To release an update:

1. Go to GitHub → Pull Requests  
2. Create a **PR from `development` → `main`**  
3. Review and merge  
4. Cloudflare will automatically deploy the update  
5. Check the site at **https://microbex.in**

---

## 5. Folder Structure (Recommended)
/assets
/css
/js
/images
/videos
/webm
/pages
index.html


Keep all visuals, videos, and scripts organized inside `assets`.

---

## 6. Testing Checklist (Before Merging)

- Check mobile responsiveness  
- Verify images and videos load  
- Test navigation links  
- Check layout in browser  
- Make sure there are no console errors

---

## 7. Workflow Summary

| Step | Tool | Action |
|------|------|--------|
| Edit code | VS Code | Make and test changes |
| Stage work | development | All updates happen here |
| Commit & Push | GitHub Desktop | Save your changes |
| Deploy | Cloudflare | Merge development → main |
| Production | main | Live website |

---

This workflow keeps the website stable and easy to maintain.


Keep all visuals, videos, and scripts organized inside `assets`.

---

## 6. Testing Checklist (Before Merging)

- Check mobile responsiveness  
- Verify images and videos load  
- Test navigation links  
- Check layout in browser  
- Make sure there are no console errors

---

## 7. Workflow Summary

| Step | Tool | Action |
|------|------|--------|
| Edit code | VS Code | Make and test changes |
| Stage work | development | All updates happen here |
| Commit & Push | GitHub Desktop | Save your changes |
| Deploy | Cloudflare | Merge development → main |
| Production | main | Live website |

---

This workflow keeps the website stable and easy to maintain.

