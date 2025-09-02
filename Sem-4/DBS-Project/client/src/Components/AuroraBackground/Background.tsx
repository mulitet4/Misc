import { AuroraBackground } from "./AuroraBackground";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";
export default function Background() {
  return (
    <AuroraBackground>
      <motion.div
        initial={{ opacity: 0.0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{
          delay: 0.3,
          duration: 0.8,
          ease: "easeInOut",
        }}
        className="relative flex flex-col gap-4 items-center justify-center px-4"
      >
        <div className="text-3xl md:text-7xl font-bold dark:text-white text-center mb-5">
          Welcome to Sri Krishna Logistics
        </div>
        {/* <div className="font-extralight text-base md:text-4xl dark:text-neutral-200 py-4">
          made by Ashrith Sathu and Ketan Goud with ❤️
        </div> */}
        <div className="flex">
          <Link
            to="/Admin"
            className="bg-black dark:bg-white rounded-full w-fit text-white dark:text-black px-4 py-2"
          >
            Administrator
          </Link>
          <Link
            to="/Manager"
            className="bg-black dark:bg-white rounded-full w-fit text-white dark:text-black px-4 py-2 ml-4"
          >
            Manager
          </Link>
        </div>
      </motion.div>
    </AuroraBackground>
  );
}
