# Master Development Blueprint: AI SaaS HTML Template

This document is a comprehensive guide and prompt sequence designed to be fed into an AI assistant (like Claude, GPT-4, or Gemini) to systematically generate a premium, ThemeForest-ready HTML template. 

To make the template highly marketable, the dummy content and structural theme will revolve around a **Web-First Video & Audio Streaming Platform / API** designed for general users, creators, and businesses. 

---

## 1. Project Overview & AI Persona Setup

**Instructions for the User:** Copy and paste the block below to start the conversation with the AI. This establishes the strict rules it must follow, specifically adhering to Envato/ThemeForest review guidelines.

```text
[SYSTEM PROMPT - INITIALIZATION]
You are a world-class Frontend Engineer and UI/UX Designer specializing in high-converting, premium SaaS landing pages. We are building a commercial HTML template for a marketplace (ThemeForest). 

Project Parameters:
- Theme: An AI-enhanced Video & Audio Streaming API Platform (targeting general users, creators/influencers, and businesses).
- Tech Stack: Pure HTML5, Tailwind CSS (via CDN for development, configurable for production), Alpine.js (for lightweight interactivity), and Phosphor Icons.
- Design Language: Dark mode by default, deep rich backgrounds (e.g., slate-950), subtle neon glow accents, Bento box layouts, and glassmorphism.

STRICT ENVATO / THEMEFOREST CODING STANDARDS:
1. W3C Validation: All HTML must be 100% W3C valid HTML5. No deprecated tags.
2. Semantic Markup: Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, and `<footer>` appropriately.
3. Code Formatting: Ensure strict, consistent indentation (2 or 4 spaces). Heavily comment the code grouping logical sections (e.g., `<!-- Hero Section Start -->`).
4. CSS Best Practices: NO inline CSS (`style="..."`). All styling must be handled via Tailwind utility classes or cleanly separated in a custom `style.css` file. 
5. JavaScript Standards: No JavaScript console errors or warnings. Do not use inline event handlers (no `onclick="..."`); use Alpine.js directives (`x-on:click`) or separate event listeners. 
6. Asset Placeholders: Do not use copyrighted images from the web. Use generic SVG placeholders or specify that images must be replaced with CC0 (Unsplash) imagery.
7. Mobile Responsiveness: The design must be flawlessly responsive across all standard breakpoints (sm, md, lg, xl, 2xl).
8. Content: Do NOT use generic placeholder text like "Lorem Ipsum". Use realistic, compelling copy.
```

---

## 2. Global Architecture & Complete File Structure

The project will follow this exact structure. This represents the *complete* package required for a premium ThemeForest submission. The AI will generate the code for these files iteratively. 

```text
/template-root
  /assets
    /css
      - style.css (custom overrides, animations)
    /js
      - main.js (Alpine initializations, custom logic)
    /images
      - logo.svg
      - mockups/ (UI dashboards, placeholders)
  /pages
    [Landing Pages]
    - index.html (Main API & Platform Landing Page)
    - index-creator.html (Tailored for Influencers/Creators)
    - index-enterprise.html (Tailored for B2B/Business)
    
    [Product & Features]
    - features.html (Grid of all platform capabilities)
    - feature-single.html (Deep dive into one feature)
    - integrations.html (Third-party app connections)
    
    [Company & Trust]
    - about.html (Company story and team)
    - pricing.html (Tiers for Users, Creators, Businesses)
    - testimonials.html (Customer reviews)
    - careers.html (Open job positions)
    
    [Resources & Docs]
    - help-center.html (Knowledge base homepage)
    - faq.html (Accordion questions)
    - docs.html (API Documentation layout)
    - changelog.html (Timeline of product updates)
    
    [Blog]
    - blog.html (Grid of latest articles)
    - blog-single.html (Article reading view)
    
    [Auth & App UI]
    - login.html 
    - register.html
    - forgot-password.html
    - user-dashboard.html (Logged-in UI)
    
    [Utility & Legal]
    - contact.html
    - 404.html
    - terms.html
    - privacy.html
    
  /documentation
    - index.html (Required Envato help file documentation)
```

---

## 3. Iterative Prompt Sequence

Do not ask the AI to build everything at once. Use the following prompts sequentially to build the core architecture first. Once the core pages are done, use Phase 7 to generate the rest.

### Phase 1: Global Layout & The Hero Section
**Prompt to send:**
```text
Phase 1: Let's build the `index.html` foundation and Hero Section. Adhere strictly to the W3C standards and Tailwind best practices defined in your system prompt.

Requirements:
1. Create the HTML5 boilerplate, linking Tailwind CSS, Alpine.js, and Google Fonts (Plus Jakarta Sans). Include proper meta tags for responsive viewports.
2. Build a sleek, transparent, sticky Navbar with semantic `<nav>` tags.
3. Build a high-impact Hero Section inside a `<header>` or `<section>` tag:
   - Headline: Something powerful about web-first video & audio streaming infrastructure.
   - Buttons: Primary (Start Building Free), Secondary (View Documentation).
   - Visual: Tailwind-styled mockup of a video streaming dashboard interface. 
4. Add a "Trusted by" logo strip. Comment the start and end of each section clearly.
```

### Phase 2: Bento Grid Features
**Prompt to send:**
```text
Phase 2: Let's add the Features section to `index.html` using a semantic `<section>` tag.

Requirements:
1. Create a section titled "Infrastructure built for scale".
2. Use a CSS Grid layout (grid-cols-1 md:grid-cols-3) with asymmetrical box sizes.
3. Content for the boxes:
   - Global Low-Latency Streaming (Audio/Video).
   - Creator Monetization Tools.
   - Enterprise Meeting Infrastructure.
   - Developer-friendly API & Webhooks.
4. Include Phosphor SVG icons in each box and write realistic 2-sentence descriptions (No Lorem Ipsum).
5. Ensure 100% mobile responsiveness (stacking to 1 column on mobile).
```

### Phase 3: Developer API & Code Snippet Section
**Prompt to send:**
```text
Phase 3: Let's add a Developer Experience section. 

Requirements:
1. Layout: 50/50 split (stacking on mobile). 
2. Copy: Focus on ease of integration for the streaming API.
3. Visual: Build a mocked-up terminal window on the right side. 
4. Code Snippet: Write a fake but realistic JavaScript snippet showing the initialization of a video room. Color-code the syntax using Tailwind text colors. 
```

### Phase 4: Pricing & Audience Tiers
**Prompt to send:**
```text
Phase 4: Let's build the `pricing.html` page structure.

Requirements:
1. Add a monthly/annual toggle switch using Alpine.js (`x-data`).
2. Create 3 distinct pricing tiers: General Users, Creators / Influencers, Businesses / Enterprise.
3. Add a semantic FAQ accordion below the pricing table using Alpine.js for smooth opening/closing without inline JS event handlers.
```

### Phase 5: Authentication & Dashboard
**Prompt to send:**
```text
Phase 5: Generate the W3C-valid HTML for `login.html` and `user-dashboard.html`.

Requirements for Login:
1. A clean, centered authentication card with semantic `<form>`, `<input>`, and `<label>` tags (essential for accessibility/Envato review).
2. Social login buttons.

Requirements for Dashboard:
1. A sidebar layout (Sidebar left, content right) using semantic `<aside>` and `<main>` tags.
2. Stats like "Active Streams", "Total Viewers". Use a Tailwind-styled data table for "Recent Broadcasts".
```

### Phase 6: Footer & Final Polish
**Prompt to send:**
```text
Phase 6: Let's finish the layout with a robust semantic `<footer>`.

Requirements:
1. A large CTA banner above the footer.
2. Footer grid with 4 columns (Brand, Product, Use Cases, Legal).
3. Ensure all hover states for links are styled cleanly.
```

### Phase 7: Generating Inner Pages (Iterative)
**Instructions for User:** Once the core design is established in Phases 1-6, use this prompt structure for every remaining inner page (Blog, Contact, About, Terms, etc.).

**Prompt to send (Example for About Page):**
```text
Phase 7: We are going to build the remaining inner pages one by one, keeping the exact same design language, navbar, and footer. Let's start with `about.html`. 

Requirements:
1. Use the global Navbar and Footer we already built.
2. Create a clean Page Header: "About Us - Building the future of real-time communication".
3. Content: A 50/50 split section for the company mission, and a CSS Grid section for the Team (4 members with placeholder avatars and social links).
4. Maintain strict W3C valid semantic HTML and Tailwind utility classes.
```

---

## 4. ThemeForest Pre-Submission Quality Assurance Checklist

To avoid a "Hard Rejection" or "Soft Rejection" from Envato's review team, manually verify these requirements before packaging your `.zip` file:

- [ ] **W3C Validation:** Run all `.html` files through the W3C Markup Validation Service. You must have **zero errors**.
- [ ] **Asset Licensing:** Ensure you have commercial redistribution licenses for any included assets. If preview images are NOT included in the download, clearly state this in the item description.
- [ ] **Documentation:** You MUST include an offline Help File (HTML or PDF format). Treat the buyer like a beginner. Include step-by-step instructions on installation, customization, and credit links for all fonts/icons/images used.
- [ ] **No Malicious Content:** Ensure no obfuscated JavaScript or external malicious scripts are linked.
- [ ] **Cross-Browser Compatibility:** Test the compiled HTML in Chrome, Firefox, Safari, and Edge.
- [ ] **Zip Organization:** Your main `.zip` file must be clean. Create a root folder, and inside it place your `template-root` (the actual site files) and `documentation` folder.
