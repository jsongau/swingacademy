#!/usr/bin/env python3
"""
Kemuel Swing Academy — static site generator.
Wraps each body fragment in /src with the shared <head>, navbar, footer,
mobile bar and scripts so every page ships crawlable, identical chrome.

Usage:  python3 build.py
"""
import os, re, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(ROOT, "src")

# ---------------------------------------------------------------- HEAD
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://kemuelswingacademy.com/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://kemuelswingacademy.com/assets/img/kemuel-logo-crest.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/kemuel-logo-shield.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow+Condensed:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/kemuel.css?v=3">
{schema}
</head>
<body>
"""

# ---------------------------------------------------------------- NAVBAR
NAV = """<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap nav__bar">
    <a class="nav__brand" href="index.html" aria-label="Kemuel Swing Academy home">
      <img src="assets/img/kemuel-logo-shield.png" alt="Kemuel Swing Academy">
      <span class="nav__brand-text">
        <span class="nav__brand-name">KEMUEL <b>SWING</b></span>
        <span class="nav__brand-tag">Train &middot; Track &middot; Find the Right Coach</span>
      </span>
    </a>
    <nav class="nav__menu" aria-label="Primary">
      <div class="nav__item">
        <a href="#" class="nav__link" aria-haspopup="true" aria-expanded="false">Train <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></a>
        <div class="mega" data-open="false">
          <a href="free-7-day.html">Free 7-Day Plan<small>Start free, no card</small></a>
          <a href="30-day-challenge.html">30-Day Swing Challenge<small>Full program — $19.99</small></a>
          <a href="play.html">🎮 Home-Run Game<small>Hit a homer, unlock the deal</small></a>
          <a href="30-day-challenge.html#gyroball">Gyroball Wrist Training</a>
          <a href="30-day-challenge.html#pitching-machine">Pitching-Machine Standards</a>
          <a href="30-day-challenge.html#box-jumps">Box Jump Progression</a>
          <a href="30-day-challenge.html#batting-practice">Batting Practice Routine</a>
          <a href="sleep-recovery.html">Sleep &amp; Recovery</a>
          <a href="nutrition.html">Baseball Nutrition Plan</a>
          <a href="progress-dashboard.html">Progress Tracker</a>
        </div>
      </div>
      <div class="nav__item">
        <a href="#" class="nav__link" aria-haspopup="true" aria-expanded="false">Find <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></a>
        <div class="mega" data-open="false">
          <a href="chino-hills-baseball-lessons.html">Baseball Lessons in Chino Hills<small>Our home city</small></a>
          <a href="coaches.html">Baseball Coaches</a>
          <a href="coaches.html?type=hitting">Hitting Coaches</a>
          <a href="coaches.html?type=pitching">Pitching Coaches</a>
          <a href="batting-cages.html">Batting Cages Near Chino Hills</a>
          <a href="baseball-tryouts.html">Baseball Tryouts</a>
          <a href="baseball-tryouts.html#clubs">AA &amp; AAA Clubs</a>
          <a href="rankings.html">🏆 Player Rankings &amp; The Climb</a>
        </div>
      </div>
      <div class="nav__item">
        <a href="#" class="nav__link" aria-haspopup="true" aria-expanded="false">For Coaches <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></a>
        <div class="mega" data-open="false">
          <a href="coach-claim.html">Claim Coach Profile<small>Get discovered by parents</small></a>
          <a href="10-session-course.html">Create 10-Session Course</a>
          <a href="coach-claim.html#leads">Get Baseball Lesson Leads</a>
          <a href="coach-claim.html#tryouts">Promote Tryout Prep</a>
          <a href="coach-claim.html#featured">Featured Coach Placement</a>
        </div>
      </div>
      <div class="nav__item">
        <a href="#" class="nav__link" aria-haspopup="true" aria-expanded="false">For Facilities <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></a>
        <div class="mega" data-open="false">
          <a href="batting-cages.html#list">List Batting Cage</a>
          <a href="batting-cages.html#claim">Claim Facility</a>
          <a href="batting-cages.html#rentals">Team Rentals</a>
          <a href="batting-cages.html#events">Host Challenge Events</a>
          <a href="reviews.html#facilities">Facility Reviews</a>
        </div>
      </div>
      <div class="nav__item">
        <a href="#" class="nav__link" aria-haspopup="true" aria-expanded="false">Tryouts <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></a>
        <div class="mega" data-open="false">
          <a href="baseball-tryouts.html?div=aa">AA Baseball Tryouts</a>
          <a href="baseball-tryouts.html?div=aaa">AAA Baseball Tryouts</a>
          <a href="baseball-tryouts.html?div=travel">Travel Ball Tryouts</a>
          <a href="baseball-tryouts.html?city=chino-hills">Chino Hills Tryouts</a>
          <a href="baseball-tryouts.html#create">Create Tryout Page</a>
        </div>
      </div>
      <div class="nav__item"><a href="reviews.html" class="nav__link">Reviews</a></div>
    </nav>
    <div class="nav__cta">
      <a href="coach-claim.html" class="btn btn--ghost-light btn--sm">List Your Program</a>
      <a href="coaches.html" class="btn btn--gold btn--sm">Find Coach</a>
      <a href="30-day-challenge.html" class="btn btn--primary btn--sm">Start Challenge</a>
    </div>
    <button class="nav__toggle" id="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-drawer"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="seam" aria-hidden="true"></div>
<div class="drawer" id="mobile-drawer" data-open="false">
  <div class="acc">
    <button class="acc__head" aria-expanded="false">Train <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></button>
    <div class="acc__panel" data-open="false">
      <a href="free-7-day.html">Free 7-Day Plan</a><a href="30-day-challenge.html">30-Day Swing Challenge</a><a href="play.html">Home-Run Game</a><a href="30-day-challenge.html#gyroball">Gyroball Wrist Training</a><a href="30-day-challenge.html#pitching-machine">Pitching-Machine Standards</a><a href="30-day-challenge.html#box-jumps">Box Jump Progression</a><a href="sleep-recovery.html">Sleep &amp; Recovery</a><a href="nutrition.html">Baseball Nutrition Plan</a><a href="progress-dashboard.html">Progress Tracker</a>
    </div>
    <button class="acc__head" aria-expanded="false">Find <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></button>
    <div class="acc__panel" data-open="false">
      <a href="chino-hills-baseball-lessons.html">Baseball Lessons in Chino Hills</a><a href="coaches.html">Baseball Coaches</a><a href="coaches.html?type=hitting">Hitting Coaches</a><a href="coaches.html?type=pitching">Pitching Coaches</a><a href="batting-cages.html">Batting Cages Near Chino Hills</a><a href="baseball-tryouts.html">Baseball Tryouts</a><a href="baseball-tryouts.html#clubs">AA &amp; AAA Clubs</a><a href="rankings.html">Player Rankings &amp; The Climb</a>
    </div>
    <button class="acc__head" aria-expanded="false">For Coaches <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></button>
    <div class="acc__panel" data-open="false">
      <a href="coach-claim.html">Claim Coach Profile</a><a href="10-session-course.html">Create 10-Session Course</a><a href="coach-claim.html#leads">Get Baseball Lesson Leads</a><a href="coach-claim.html#tryouts">Promote Tryout Prep</a><a href="coach-claim.html#featured">Featured Coach Placement</a>
    </div>
    <button class="acc__head" aria-expanded="false">For Facilities <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></button>
    <div class="acc__panel" data-open="false">
      <a href="batting-cages.html#list">List Batting Cage</a><a href="batting-cages.html#claim">Claim Facility</a><a href="batting-cages.html#rentals">Team Rentals</a><a href="batting-cages.html#events">Host Challenge Events</a><a href="reviews.html#facilities">Facility Reviews</a>
    </div>
    <button class="acc__head" aria-expanded="false">Tryouts <svg viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></button>
    <div class="acc__panel" data-open="false">
      <a href="baseball-tryouts.html?div=aa">AA Baseball Tryouts</a><a href="baseball-tryouts.html?div=aaa">AAA Baseball Tryouts</a><a href="baseball-tryouts.html?div=travel">Travel Ball Tryouts</a><a href="baseball-tryouts.html?city=chino-hills">Chino Hills Tryouts</a><a href="baseball-tryouts.html#create">Create Tryout Page</a>
    </div>
    <a class="acc__head" href="reviews.html" style="border-bottom:1px solid rgba(255,255,255,.12)">Reviews</a>
  </div>
  <div class="drawer__cta">
    <a href="30-day-challenge.html" class="btn btn--primary btn--block btn--lg">Start the 30-Day Challenge</a>
    <a href="coaches.html" class="btn btn--gold btn--block">Find a Coach</a>
    <a href="coach-claim.html" class="btn btn--ghost-light btn--block">List Your Coaching Program</a>
  </div>
</div>
"""

# ---------------------------------------------------------------- FOOTER
FOOTER = """<div class="seam seam--gold" aria-hidden="true"></div>
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="assets/img/kemuel-logo-crest.png" alt="Kemuel Swing Academy">
        <p>A Chino Hills-first youth baseball training ecosystem. Train the swing, track the growth, and find the right coach.</p>
      </div>
      <div>
        <h4>Kemuel Swing Academy</h4>
        <a href="index.html">Home</a><a href="free-7-day.html">Free 7-Day Plan</a><a href="30-day-challenge.html">30-Day Challenge</a><a href="play.html">Home-Run Game</a><a href="checkout.html">Get the 30-Day Guide</a><a href="progress-dashboard.html">Progress Log</a><a href="reviews.html">Reviews</a>
      </div>
      <div>
        <h4>Baseball Lessons</h4>
        <a href="chino-hills-baseball-lessons.html">Baseball Lessons in Chino Hills</a><a href="coaches.html?type=hitting&amp;city=chino-hills">Hitting Coach in Chino Hills</a><a href="coaches.html?type=pitching&amp;city=chino-hills">Pitching Lessons in Chino Hills</a><a href="chino-hills-baseball-lessons.html#training">Youth Baseball Training in Chino Hills</a><a href="chino-hills-baseball-lessons.html#tryouts">Tryout Prep in Chino Hills</a><a href="coaches.html">Private Baseball Lessons in Southern California</a>
      </div>
      <div>
        <h4>Find Baseball Help</h4>
        <a href="coaches.html">Baseball Coach Directory</a><a href="batting-cages.html">Batting Cage Directory</a><a href="baseball-tryouts.html?div=aa">AA Baseball Tryouts</a><a href="baseball-tryouts.html?div=aaa">AAA Baseball Tryouts</a><a href="rankings.html">Player Rankings &amp; The Climb</a><a href="10-session-course.html">10-Session Coaching Course</a>
      </div>
      <div>
        <h4>For Coaches &amp; Facilities</h4>
        <a href="coach-claim.html">Claim Coach Profile</a><a href="coach-claim.html#list">List Coaching Program</a><a href="10-session-course.html">Create 10-Session Course</a><a href="batting-cages.html#list">List Batting Cage</a><a href="baseball-tryouts.html#create">Create Tryout Page</a>
      </div>
    </div>
    <div class="footer__grid" style="grid-template-columns:1fr;margin-top:40px">
      <div>
        <h4>Southern California Areas We Serve</h4>
        <div class="pill-row" style="gap:8px 18px">
          <a href="chino-hills-baseball-lessons.html">Chino Hills</a><a href="coaches.html?city=chino">Chino</a><a href="coaches.html?city=diamond-bar">Diamond Bar</a><a href="coaches.html?city=pomona">Pomona</a><a href="coaches.html?city=ontario">Ontario</a><a href="coaches.html?city=rancho-cucamonga">Rancho Cucamonga</a><a href="coaches.html?region=orange-county">Orange County</a><a href="coaches.html?region=inland-empire">Inland Empire</a><a href="coaches.html?region=la-county">Los Angeles County</a><a href="coaches.html?region=san-diego">San Diego County</a>
        </div>
      </div>
    </div>
    <div class="footer__seo">
      Kemuel Swing Academy connects families searching for baseball lessons in Chino Hills, youth hitting coaches, batting cages near Chino Hills, travel baseball tryouts, and private baseball training across Southern California. Built for serious baseball families who want structure, discipline, and visible progress.
    </div>
    <div class="footer__bottom">
      <span style="font-size:.85rem;color:#7E8B9B">&copy; 2026 Kemuel Swing Academy. All rights reserved.</span>
      <div class="footer__social" aria-label="Social links">
        <a href="#" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg></a>
        <a href="#" aria-label="YouTube"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="2" y="5" width="20" height="14" rx="4" stroke="currentColor" stroke-width="2"/><path d="M10 9l5 3-5 3V9Z" fill="currentColor"/></svg></a>
        <a href="#" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M14 8h2V5h-2a3 3 0 0 0-3 3v2H9v3h2v6h3v-6h2l1-3h-3V8a1 1 0 0 1 1-1Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></a>
      </div>
    </div>
  </div>
  <div class="footer__safety">
    <div class="wrap">
      Kemuel Swing Academy is a youth baseball training and discovery platform. It does not guarantee home runs, scholarships, roster spots, tryout selection, or injury prevention. Public coach, cage, and club listings are based on publicly available information and are not endorsements unless the profile is claimed and verified. Players should train with parent or coach supervision and stop if pain occurs. Sleep and nutrition guidance is educational, not medical advice.
    </div>
  </div>
</footer>
<div class="mobile-bar">
  <a href="checkout.html#program"><svg viewBox="0 0 24 24" fill="none"><path d="M5 3l14 9-14 9V3Z" fill="currentColor"/></svg> Get 30-Day $19.99</a>
  <a href="play.html"><svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/><path d="M12 7v10M7 12h10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg> Play &amp; Win</a>
</div>
<script src="assets/js/kemuel.js"></script>
</body>
</html>
"""

# ---------------------------------------------------------------- PAGE META
PAGES = {
 "index": dict(
    title="Kemuel Swing Academy | Youth Baseball Training & Coaches in Chino Hills",
    desc="Chino Hills-first youth baseball training ecosystem. Start the 30-day swing challenge, track visible progress, find hitting coaches, batting cages, and AA/AAA tryouts across Southern California."),
 "chino-hills-baseball-lessons": dict(
    title="Baseball Lessons in Chino Hills | Youth Coaches, Batting Cages & Tryouts",
    desc="Find baseball lessons in Chino Hills: youth hitting coaches, batting cages, tryout prep, and the 30-day Kemuel Swing Academy training challenge. Built for Chino Hills baseball families."),
 "30-day-challenge": dict(
    title="30-Day Baseball Swing Challenge | Kemuel Swing Academy",
    desc="A structured 30-day youth baseball training challenge: gyroball wrist work, pitching-machine cage standards, box jumps, rotational strength, recovery, and progress tracking. Train smart, not exhausted."),
 "progress-dashboard": dict(
    title="Player Progress Dashboard | Track the 30-Day Journey",
    desc="Track gyroball streaks, pitching-machine sessions, box jumps, cage logs, hard-contact and confidence scores, sleep, and nutrition. Make your young hitter's progress visible."),
 "growth-projection": dict(
    title="Player Growth Projection | Stats + Discipline Forecast",
    desc="Stats show what happened. Discipline predicts what can happen next. See discipline score, player type, 30 and 90-day projections, and the next best training step."),
 "coaches": dict(
    title="Baseball Coach Directory | Hitting & Pitching Coaches in SoCal",
    desc="Find baseball coaches in Chino Hills and Southern California. Filter by city, position, age group, and budget, then match with a hitting, pitching, or tryout-prep coach."),
 "coach-claim": dict(
    title="Claim Your Coach Profile | Get Baseball Lesson Leads",
    desc="Get more baseball players without chasing parents on Instagram. Claim your coach profile, sell 10-session courses, promote tryout prep, and receive booking requests."),
 "10-session-course": dict(
    title="10-Session Private Baseball Coaching Course | Player Development Plan",
    desc="Stop buying random lessons. The 10-session course gives young players a structured development plan with a baseline, weekly focus, and final evaluation."),
 "batting-cages": dict(
    title="Batting Cages Near Chino Hills | SoCal Batting Cage Directory",
    desc="Find batting cages near Chino Hills and across Southern California. Filter by indoor/outdoor, pitching machine, lessons, weekend hours, and team rentals. Log sessions to your 30-day journey."),
 "baseball-tryouts": dict(
    title="Baseball Tryouts in Southern California | AA, AAA & Travel Ball",
    desc="Find AA, AAA, and travel baseball tryouts near Chino Hills and across SoCal. View tryout dates, fees, positions needed, and sign up. Clubs can create tryout pages."),
 "sleep-recovery": dict(
    title="Sleep, Rest & Recovery for Young Baseball Players",
    desc="Stronger swings are built in training but improved in recovery. Sleep, rest-day logic, and recovery guidance for young baseball players. Train smart, not exhausted."),
 "nutrition": dict(
    title="Baseball Nutrition Plan for Young Players | Pre-Cage & Recovery Meals",
    desc="Simple baseball nutrition guidance for young players: pre-cage meals, quick snacks, recovery food, and a sample training-day plan. Fuel, not extreme diets."),
 "reviews": dict(
    title="Reviews & Player Stories | Kemuel Swing Academy",
    desc="Parent reviews, player stories, coach testimonials, and facility feedback from Kemuel Swing Academy baseball families. Real progress, not fake perfection."),
 "checkout": dict(
    title="Get Started | Free 7-Day Plan, 30-Day Program & Gyroball",
    desc="Start the free 7-day swing plan, unlock the full 30-day program for $19.99 (was $99.99), and get the gyroball wrist trainer. Build a better hitter and a more disciplined student."),
 "free-7-day": dict(
    title="Free 7-Day Baseball Swing Plan for Young Players | Kemuel Swing Academy",
    desc="Get a free 7-day youth baseball swing plan: daily gyroball wrist work, swing reps, and a progress checklist parents and players do together. No card required."),
 "play": dict(
    title="Home-Run Timing Game | Hit a Homer, Unlock the 30-Day Deal",
    desc="Play the Kemuel Swing Academy home-run timing game. Time your swing, hit a home run, and unlock the 30-day training program for $19.99 plus a free coach session."),
 "rankings": dict(
    title="Kemuel Player Rankings & The Climb | Youth Baseball Leaderboard",
    desc="Get your player on the Kemuel Player Rankings. Climb from rec ball to travel, AA, AAA, and beyond. Discipline-score leaderboard, shareable player cards, and a monthly Hall of Fame."),
}

def build():
    count = 0
    for slug, meta in PAGES.items():
        body_path = os.path.join(SRC, slug + ".html")
        if not os.path.exists(body_path):
            print(f"  skip (no src): {slug}")
            continue
        with open(body_path, encoding="utf-8") as f:
            raw = f.read()
        # Optional schema block: lines wrapped in <!--SCHEMA ... SCHEMA-->
        schema = ""
        m = re.search(r"<!--SCHEMA\s*(.*?)\s*SCHEMA-->", raw, re.S)
        if m:
            schema = m.group(1).strip()
            raw = raw.replace(m.group(0), "").strip()
        head = HEAD.format(title=html.escape(meta["title"]),
                           desc=html.escape(meta["desc"]),
                           slug=(slug + ".html") if slug != "index" else "",
                           schema=schema)
        out = head + NAV + "\n<main id=\"main\">\n" + raw + "\n</main>\n" + FOOTER
        with open(os.path.join(ROOT, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(out)
        count += 1
        print(f"  built: {slug}.html")
    print(f"Done. {count} pages.")

if __name__ == "__main__":
    build()
