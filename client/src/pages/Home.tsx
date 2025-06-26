import Layout from "@/components/Layout";
import { FaGithub, FaLinkedin, FaEnvelope, FaFacebookF } from "react-icons/fa";
import avatarImg from "@/assets/avatar.jpg";
import avatarFrame from "@/assets/profile_frame.png";

export default function Home() {
  return (
    <Layout>
      <div className="flex flex-col items-center justify-center h-full text-white text-center relative z-10">
        {/* Avatar */}
        <div className="relative w-24 h-24 sm:w-32 sm:h-32 md:w-40 md:h-40 overflow-hidden">
          <img
            src={avatarImg}
            alt="Kenson Manduyag"
            className="absolute top-1/2 left-1/2 w-20 h-20 sm:w-28 sm:h-28 md:w-32 md:h-32 object-cover -translate-x-1/2 -translate-y-1/2 rounded-none"
          />
          <img
            src={avatarFrame}
            alt="Profile Frame"
            className="absolute top-0 left-0 w-full h-full object-cover pointer-events-none"
          />
        </div>

        {/* Name and Subtitle */}
        <h1 className="text-xl sm:text-2xl md:text-3xl lg:text-4xl font-bold mt-4">Kenson Manduyag</h1>
        <p className="text-sm sm:text-base md:text-lg mb-4">Software Developer · Photographer · Gamer</p>

        {/* Social Icons */}
        <div className="flex gap-4 justify-center">
          <a
            href="https://www.facebook.com/kvnianmndyg"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-blue-500 transition"
            aria-label="Facebook"
          >
            <FaFacebookF size={20} className="sm:size-[24px]" />
          </a>
          <a
            href="https://github.com/mynameiskenson"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-gray-300 transition"
            aria-label="GitHub"
          >
            <FaGithub size={20} className="sm:size-[24px]" />
          </a>
          <a
            href="https://www.linkedin.com/in/kensonmanduyag"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-blue-300 transition"
            aria-label="LinkedIn"
          >
            <FaLinkedin size={20} className="sm:size-[24px]" />
          </a>
          <a
            href="mailto:kvniancrndo@gmail.com"
            className="hover:text-red-300 transition"
            aria-label="Email"
          >
            <FaEnvelope size={20} className="sm:size-[24px]" />
          </a>
        </div>
      </div>
    </Layout>
  );
}