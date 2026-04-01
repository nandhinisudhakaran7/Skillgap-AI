// LOGIN
function login() {
    window.location.href = "dashboard.html";
}

// UPLOAD FORM
document.getElementById("uploadForm")?.addEventListener("submit", async function (e) {

    e.preventDefault(); // ✅ FIRST LINE

    console.log("FORM SUBMITTED");

    let resumeFile = document.getElementById("resume").files[0];
    let jobFile = document.getElementById("job").files[0];

    // ✅ CHECK FILES
    if (!resumeFile || !jobFile) {
        alert("Please upload both files!");
        return;
    }

    let formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job", jobFile);

    try {
        const res = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData
        });

        console.log("RESPONSE STATUS:", res.status);

        // ❌ If API fails
        if (!res.ok) {
            throw new Error("Server error");
        }

        const data = await res.json();

        console.log("API RESPONSE:", data);

        // ✅ SAVE ONLY REAL DATA (IMPORTANT)
        localStorage.setItem("result", JSON.stringify(data));

        // ✅ REDIRECT
        window.location.href = "result.html";

    } catch (error) {
        console.error("Upload error:", error);

        alert("Backend not connected OR server error!");

        // 🔥 TEMP FALLBACK (so UI still works)
        localStorage.setItem("result", JSON.stringify({
            match_percent: 75,
            matched_skills: ["python"],
            missing_skills: ["aws"],
            resume_skills: ["python"],
            job_skills: ["python", "aws"]
        }));

        window.location.href = "result.html";
    }
});