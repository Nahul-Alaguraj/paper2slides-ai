// frontend/app/page.tsx
import UploadBox from "@/components/uploadbox";

export default function Home() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-gray-50">
      <div className="w-full max-w-3xl p-6">
        <h1 className="text-3xl font-bold mb-4 text-black">AI Paper-to-Slides Generator</h1>
        <p className="mb-6 text-gray-600">Upload a PDF and we'll extract the content.</p>
        <UploadBox />
      </div>
    </main>
  );
}
