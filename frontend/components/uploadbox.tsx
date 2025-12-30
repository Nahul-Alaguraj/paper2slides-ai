// frontend/components/UploadBox.tsx
"use client";

import { useState } from "react";

export default function UploadBox() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const onFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setResult(null);
    setError(null);
    const f = e.target.files?.[0] ?? null;
    setFile(f);
  };

  const onUpload = async () => {
    if (!file) return setError("Choose a file first.");
    setUploading(true);
    setError(null);
    setResult(null);

    try {
      const form = new FormData();
      form.append("file", file);

      const res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: form,
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`${res.status} ${text}`);
      }

      const json = await res.json();
      setResult(json);
    } catch (err: any) {
      setError(err?.message ?? "Upload failed");
    } finally {
      setUploading(false);
    }
  };


  const onDownloadPPT = async () => {
    if (!result?.slides?.slides) return;

    const res = await fetch("http://127.0.0.1:8000/generate-ppt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        slides: result.slides.slides,
      }),
    });

    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "ai_generated_slides.pptx";
    document.body.appendChild(a);
    a.click();
    a.remove();
  };

  return (
    <div className="max-w-2xl w-full p-6 bg-white rounded-lg shadow text-black">
      <h2 className="text-xl font-semibold mb-3">
        Upload a research paper (PDF)
      </h2>

      <input
        id="file"
        type="file"
        accept="application/pdf"
        onChange={onFileChange}
        className="mb-4"
      />

      <div className="flex gap-3">
        <button
          onClick={onUpload}
          disabled={!file || uploading}
          className="px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50"
        >
          {uploading ? "Uploading..." : "Upload"}
        </button>

        <button
          onClick={() => {
            setFile(null);
            setResult(null);
            setError(null);
            (
              document.getElementById("file") as HTMLInputElement | null
            )!.value = "";
          }}
          className="px-4 py-2 border border-black rounded"
        >
          Reset
        </button>
      </div>

      {error && <p className="mt-3">Error: {error}</p>}

      {result?.slides?.slides && (
        <>
          <div className="mt-6 space-y-6">
            {result.slides.slides.map((slide: any, i: number) => (
              <div key={i} className="p-4 border rounded">
                <h3 className="font-semibold text-lg mb-2">
                  {slide.title}
                </h3>

                <ul className="list-disc ml-5">
                  {Array.isArray(slide.bullets) &&
                    slide.bullets.map((b: string, j: number) => (
                      <li key={j}>{b}</li>
                    ))}
                </ul>
              </div>
            ))}
          </div>

          {/* 🔽 Download button */}
          <div className="mt-6">
            <button
              onClick={onDownloadPPT}
              className="px-5 py-2 bg-green-600 text-white rounded"
            >
              Download PPT
            </button>
          </div>
        </>
      )}
    </div>
  );
}
