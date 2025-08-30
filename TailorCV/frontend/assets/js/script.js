
  // --- Helpers ---
  const $ = (sel) => document.querySelector(sel);
  const jobDesc = $('#jobDesc');
  const cvInput = $('#cvInput');
  const fileList = $('#fileList');
  const drop = $('#drop');
  const analyzeBtn = $('#analyzeBtn');
  const loading = $('#loading');
  const errorBox = $('#error');
  const recList = $('#recList');
  const matchSummary = $('#matchSummary');
  const keywordsWrap = $('#keywords');

  // Sample JD for quick demo
  const SAMPLE_JD = `We are seeking a Senior Machine Learning Engineer with experience in Python, NLP, LLMs (OpenAI, Azure OpenAI), LangChain, vector databases, and cloud platforms (Azure or AWS). Responsibilities include building data pipelines, fine-tuning models, prompt engineering, and deploying services with Docker/Kubernetes and CI/CD. Bonus: experience with FastAPI, SQL, and MLOps.`;

  $('#sampleBtn').addEventListener('click', () => {
    jobDesc.value = SAMPLE_JD;
    jobDesc.focus();
  });

  // Uploader: show selected file
  cvInput.addEventListener('change', () => {
    fileList.textContent = cvInput.files[0] ? `Selected: ${cvInput.files[0].name}` : '';
  });

  // Drag & Drop UX
  ['dragenter','dragover'].forEach(evt => {
    drop.addEventListener(evt, e => { e.preventDefault(); e.stopPropagation(); drop.classList.add('dragover'); });
  });
  ['dragleave','drop'].forEach(evt => {
    drop.addEventListener(evt, e => { e.preventDefault(); e.stopPropagation(); drop.classList.remove('dragover'); });
  });
  drop.addEventListener('drop', (e) => {
    const file = e.dataTransfer.files && e.dataTransfer.files[0];
    if(file){
      cvInput.files = e.dataTransfer.files; // attach to input
      fileList.textContent = `Selected: ${file.name}`;
    }
  });

 analyzeBtn.addEventListener('click', async () => {
  errorBox.style.display = 'none';
  recList.innerHTML = '';
  matchSummary.style.display = 'none';
  keywordsWrap.innerHTML = '';

  const jdText = jobDesc.value.trim();
  if(!jdText){
    return showError('Please paste the Job Description first.');
  }

  if(!cvInput.files[0]){
    console.warn('No CV uploaded – proceeding with JD-only analysis.');
  }

  setLoading(true);
  try{
   
    const data = await runAnalysis(jdText, cvInput.files[0]);
    renderResults(data);
    document.getElementById('results').scrollIntoView({behavior:'smooth'});
  }catch(err){
    console.error(err);
    showError('Something went wrong while analyzing. Please try again.');
  }finally{
    setLoading(false);
  }
});

  function setLoading(state){
    loading.style.display = state ? 'flex' : 'none';
    analyzeBtn.disabled = state;
  }
  function showError(msg){
    errorBox.textContent = msg;
    errorBox.style.display = 'block';
  }

  // --- Mock Analysis (local heuristic) ---
  async function mockAnalysis(jd){
    await new Promise(r => setTimeout(r, 900)); // simulate latency
    const SKILLS = [
      'Python','JavaScript','TypeScript','FastAPI','Flask','React','Node','SQL','PostgreSQL','MongoDB',
      'AWS','Azure','GCP','Docker','Kubernetes','CI/CD','GitHub Actions','Terraform',
      'Machine Learning','Deep Learning','NLP','LLM','LLMs','OpenAI','Azure OpenAI','LangChain','Vector DB','Pinecone',
      'Prompt Engineering','MLOps'
    ];

    const found = [];
    const lower = jd.toLowerCase();
    for(const s of SKILLS){ if(lower.includes(s.toLowerCase())) found.push(s); }

    // Simple keyword-based suggestions
    const recs = [];
    if(found.includes('NLP') || found.includes('LLM') || found.includes('LLMs')){
      recs.push('Add a projects subsection titled "LLM/NLP Projects" with 2–3 bullet points quantifying impact (e.g., \'Reduced support tickets 22% using RAG with LangChain and OpenAI\').');
      recs.push('Include key terms in your summary: "NLP", "LLMs", "prompt engineering", and any frameworks you used (LangChain, Transformers).');
    }
    if(found.includes('Docker')){
      recs.push('Under Tech Stack, group DevOps tools together: Docker • Kubernetes • CI/CD. Mention images size reductions or deployment speed if applicable.');
    }
    if(found.includes('Azure') || found.includes('AWS')){
      recs.push('Create a "Cloud" line with the specific services you used (e.g., Azure OpenAI, AKS, S3, Lambda). Avoid generic "Worked on cloud" phrasing.');
    }
    if(found.includes('SQL')){
      recs.push('Quantify data scale (tables/rows) and performance wins (e.g., optimized SQL reducing query time from 1.3s → 220ms).');
    }
    if(found.includes('LangChain')){
      recs.push('If you built RAG, list: embedding model, vector DB, chunking, and evaluation metrics (precision/recall).');
    }
    if(recs.length === 0){
      recs.push('Mirror 6–10 exact keywords from the JD across your summary, experience bullets, and skills section (ATS friendly).');
      recs.push('For each responsibility in JD, map 1 bullet in your experience using STAR (Situation, Task, Action, Result).');
      recs.push('Keep bullets impact-first: start with a strong verb + metric (e.g., "Increased", "Reduced", "Automated").');
    }

    // Create short keyword list (unique)
    const topKeywords = [...new Set(found)].slice(0, 14);

    return {
      matchScore: Math.min(98, Math.round((topKeywords.length/12)*100)),
      keywords: topKeywords,
      recommendations: recs
    };
  }
async function runAnalysis(jdText, file){
  const form = new FormData();
  form.append('job_description', jdText);
  if(file) form.append('cv', file);

  const res = await fetch('http://127.0.0.1:5000/analyze', { 
    method:'POST', 
    body: form 
  });
  
  if(!res.ok) throw new Error('API error');
  return await res.json(); 
  
}


  // --- Render ---
  function renderResults(data){
  matchSummary.style.display = 'inline-flex';
  matchSummary.textContent = `Estimated match: ${data.matchScore}%`;

  if(data.keywords?.length){
    keywordsWrap.innerHTML = '<div class="muted" style="margin:8px 0 4px">Detected keywords:</div>' +
      data.keywords.map(k=>`<span class="pill">${escapeHtml(k)}</span>`).join('');
  }

  recList.innerHTML = (data.recommendations||[]).map(text => `
    <li class="rec-item">
      <div class="dot" aria-hidden="true"></div>
      <div>${escapeHtml(text)}</div>
    </li>
  `).join('');

  // --- 🎉 Launch celebration animation ---
  triggerCelebration();
}

function triggerCelebration(){
  // confetti burst
  confetti({
    particleCount: 200,
    spread: 100,
    origin: { y: 0.6 }
  });

  // fireworks style repeating for 2 seconds
  let duration = 2 * 1000;
  let end = Date.now() + duration;

  (function frame() {
    confetti({
      particleCount: 5,
      angle: 60,
      spread: 55,
      origin: { x: 0 }
    });
    confetti({
      particleCount: 5,
      angle: 120,
      spread: 55,
      origin: { x: 1 }
    });

    if (Date.now() < end) {
      requestAnimationFrame(frame);
    }
  }());
}


  function escapeHtml(str){
    return str.replace(/[&<>"']/g, (c)=> ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','\'':'&#39;'}[c]));
  }